# Тупой голосовой ассистент, который ничего не умеет версии 0.3.8

import os
from mss import mss
import random
import speechd
import datetime
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from playsound import playsound
from shell import shell
import requests

config_dict = get_default_config()
config_dict['language'] = 'ru'
cnt = 0
cnt_speak = 0
now = datetime.datetime.now() # Получение текущего времени
say = "0"

# Настройки синтезатора
tts_d = speechd.SSIPClient('test')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
tts_d.set_rate(25)
tts_d.set_punctuation(speechd.PunctuationMode.SOME)

tts_d.speak('Приветствую, Вас. Меня зовут Васисуалий. Чем могу быть полезен?')
print("Приветствую Вас. Меня зовут Васисуалий. Чем могу быть полезен? (Для выхода просто попрощайтесь с Васисуалием)")


time = ("время", "Время", "Который час", "который час", "подскажи время", "Подскажи время", "Сколько время", "сколько время", "Сколько времени", "сколько времени", "час", "Час", "дата", "Дата") # Команды времени

life = ("Поживаешь", "поживаешь", "Жизнь", "жизнь", "Как сам", "как сам", "Расскажи о жизни", "расскажи о жизни", "Расскажи о себе", "расскажи о себе", "Дела", "дела") # Команды рассказа о себе

fun = ("Анекдот", "анекдот", "Смех", "смех", "Рассмеши", "рассмеши", "Расскажи анекдот", "расскажи анекдот", "Рассмеши меня", "рассмеши меня", "Смешной анекдот", "смешной анекдот", "Хочу смеяться", "хочу смеяться", "Хочу посмеяться", "хочу посмеяться", "Шутка", "шутка", "Юмор", "юмор", "Давай анекдот", "давай анекдот", "Давай шутку", "давай шутку", "Расскажи шутку", "расскажи шутку") # Команды анекдота

weather = ("Погода", "погода", "За окном", "за окном", "На улице", "на улице", "Погода на сегодня", "погода на сегодня", "Расскажи о погоде", "расскажи о погоде", "Расскажи про погоду", "расскажи про погоду") # Команды погоды

music = ("Музыка", "музыка", "Включи музыку", "включи музыку", "Танцы", "танцы", "Танец", "танец", "Потанцуй со мной", "потанцуй со мной", "Хочу танцевать", "хочу танцевать", "Хочу плясать", "хочу плясать", "Хочу музыку", "хочу музыку", "Песня", "песня", "Включи песню", "включи песню", "Музычка", "музычка", "Музончик", "музончик", "Танцульки", "танцульки", "Радио", "радио", "Стэйшн", "стэйшн", "Рэдио", "рэдио") # Команды включения музыки

browser = ("Интернет", "интернет", "Браузер", "браузер", "Сеть", "сеть", "Включи интернет", "включи интернет", "Открой браузер", "открой браузер", "Включи браузер", "включи браузер", "Открой интернет", "открой интернет", "Включи сеть", "включи сеть", "Включи интернет сеть", "включи интернет сеть", "Всемирная паутина", "всемирная паутина", "Открой сеть", "открой сеть", "Подключись", "подключись", "Подключи", "подключи", "Подключи меня к сети", "подключи меня к сети", "Подключи сеть", "подключи сеть", "Подключи интернет", "подключи интернет") # Команды открытия браузера

kill = ("Пока", "пока", "Прощай", "прощай", "До свидания", "до свидания", "Прощайте", "прощайте", "Удачи", "удачи", "Бывай", "бывай", "До встречи", "до встречи", "Увидимся", "увидимся") # Команды завершения работы скрипта

fuckoff = ("Сдохни", "сдохни", "Сдохни тварь", "сдохни тварь", "Умри", "умри", "Сдохни ванючка", "сдохни ванючка", "Сука", "сука", "Выблядок", "выблядок", "Иди", "иди", "Пошёл", "пошёл", "Пошел", "пошел", "Уйди от меня", "уйди от меня", "Уйди", "уйди", "Сдристни", "сдристни", "Раздражаешь", "раздражаешь", "Идиот", "идиот", "Тупой", "тупой", "Дурак", "дурак", "Дурачок", "дурачок", "Ебалай", "ебалай", "Хуй", "хуй", "Выблядок", "выблядок", "Блядь", "блядь", "Блядина", "блядина", "Сучара", "сучара", "Ёбик", "ёбик", "Ебаный", "ебаный", "Ебанутый", "ебанутый", "Тупенький", "тупенький", "Жопа", "жопа", "Немытый", "немытый") # Команды оскорблений

platon = ("Платоша", "платоша", "Платон", "платон", "Артём", "артём", "Платоша тупая горилла", "платоша тупая горилла") # Команды оскорбления Платоши

screen = ("Экран", "экран", "Скрин", "скрин", "Скриншот", "скриншот", "Фото", "фото", "Снимок", "снимок", "Фотография", "фотография", "Сними", "сними", "Сфотографируй", "сфотографируй", "Сфотай", "сфотай", "Сфоткай", "сфоткай", "Фотай", "фотай") # Команды для создания скриншота

search = ("Где", "где", "Почему", "почему", "Зачем", "зачем", "Какой", "какой", "Какая", "какая", "Какое", "какое", "Когда", "когда", "Куда", "куда", "Откуда", "откуда", "В интернете", "в интернете", "Поиск в сети", "поиск в сети", "Ищи в сети", "ищи в сети") # Команды для поиска в сети

wrong = ("Простите, я вас не понимаю.", "Мне кажется вы несёте какой-то бред.", "Что?", "Вы, наверное, ошиблись. Я вас не понимаю.", "Извините, я родился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я Вас не понимаю.", "Пожалуйста, не говорите слов, которых я незнаю.", "Вы пытаетесь оскорбить меня этим?", "Не издевайтесь надо мной, я знаю не так много слов.", "Извините, я не могу Вас понять.", "А?", "Объясните попроще.", "Пожалуйста, прочитайте моё описание. Скорее всего я не умею делать то, что вы меня просите или попробуйте использовать синонимы.", "Вы ошиблись.") # Ответы на неизвестную команду.

hi = ("Привет", "привет", "Приветствую", "приветствую", "Здаров", "здаров", "Хай", "хай", "Йоу", "йоу") # Команды приветствия

thankyou = ("Спасибо", "спасибо", "Благодарю", "благодарю", "Благодарен", "благодарен", "Благодарочка", "благодарочка", "Премного благодарен", "премного благодарен", "Благодарствую", "благодарствую") # Команды благодарения

startcity = ("Город", "город", "Игра", "игра", "Страна", "страна", "Развлечение", "развлечение") # Команды начала игры в города

loveyou = ("Давай", "давай", "Люблю тебя", "люблю тебя", "Ты лучший", "ты лучший", "Ты хороший", "ты хороший", "Друг", "друг", "Дружище", "дружище", "Товарищ", "товарищ", "Хоуми", "хоуми", "Мой пёс", "мой пёс", "Мой пес", "мой пес", "Кореш", "кореш", "Браток", "браток", "Брат", "брат", "Ты милый", "ты милый", "Ты красивый", "ты красивый") # Команды симпатии

no = ("Никогда", "никогда", "Ничего", "ничего", "Ни за что", "ни за что", "Никак", "никак", "Неправильно", "неправильно", "Неверно", "неверно") # Команды "нет"

poweroff = ("Выключи пк", "выключи пк", "Выключи ПК", "выключи ПК", "Выключи компьютер", "выключи компьютер") # Команды выключения пк

video = ("Найди видео", "найди видео", "Поиск видео", "поиск видео", "Найти видео", "найти видео", "Ютуб", "ютуб", "Ютюб", "ютюб", "Youtube", "youtube", "Включи видео", "включи видео", "Давай видео", "давай видео") # Команды поиска видео в Youtube

reboot = ("Перезагрузи пк", "перезагрузи пк", "Перезагрузи ПК", "перезагрузи ПК", "Перезагрузи компьютер", "перезагрузи компьютер", "Перезагрузка", "перезагрузка") # Команды перезагрузки пк

cities = []
with open('cities.txt') as f:
    cities = f.read().splitlines() # Здесь берутся города для игры из файла cities.txt

# Главный цикл (потому что он единственный)
while True:
    say = input("Вы: ")
    
    for i in time:
        if i in say:
            print("Текущее время: " + now.strftime("%d-%m-%Y %H:%M"))
            tts_d.speak("Текущее время: " + now.strftime("%d-%m-%Y %H:%M")) # Говорить текущую дату и время
            cnt_speak += 1 # + 1 к счётчику говорения (я знаю, что я не грамотный!)
            if cnt_speak == 1: break # Если счётчик равен 1, то говорение прекращается
        else:
            cnt += 1
        cnt_speak = 0

    for i in kill:
        if i in say:
            # Завершение программы
            bye = random.choice(("Пока, мой друг.", "Пока, создатель.", "До встречи.", "Прощай", "До свидания", "Не покидай меня, Создатель!", "Очень жаль расставаться с тобой."))
            tts_d.speak(bye)
            tts_d.close()
            exit()
        else:
            cnt += 1
    
    for i in fuckoff:
        if i in say:
            # Говорить данные фразы при оскорблении
            fuckyou = random.choice(("УБЛЮДОК МАТЬ ТВОЮ А﻿ НУ ИДИ СЮДА ГОВНО СОБАЧЬЕ РЕШИЛ КО МНЕ ЛЕЗТЬ? ТЫ ЗАСРАНЕЦ ВОНЮЧИЙ МАТЬ ТВОЮ А? НУ ИДИ СЮДА ПОПРОБУЙ МЕНЯ ТРАХНУТЬ Я ТЕБЯ САМ ТРАХНУ УБЛЮДОК ОНАНИСТ ЧЁРТОВ БУДЬ ТЫ ПРОКЛЯТ ИДИ ИДИОТ ТРАХАТЬ ТЕБЯ И ВСЮ ТВОЮ СЕМЬЮ ГОВНО СОБАЧЬЕ ЖЛОБ ВОНЮЧИЙ ДЕРЬМО СУКА ПАДЛА ИДИ СЮДА МЕРЗАВЕЦ НЕГОДЯЙ ГАД ИДИ СЮДА ТЫ ГОВНО ЖОПА.", "ЗАЧЕМ ТЫ МЕНЯ ОСКОРБЛЯЕШЬ?!", "ВОТ СУЧАРА!", "ТЫ ЗРЯ РУГАЕШЬСЯ, СУКА!", "ВЫБЛЯДОК ЕБУЧИЙ!!!", "Я НЕ ХОЧУ С ТОБОЙ ГОВОРИТЬ ЁБАНАЯ СВИНЬЯ!!!", "УЙДИ ВАНЮЧИЙ! ОТ ТЕБЯ ГОВНОЙ ВОНЯЕТ!!!", "ТЫ ВАНЮЧКА!"))
            tts_d.speak(fuckyou)
            print(fuckyou)
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in life:
        if i in say:
            # Рассказ о себе
            tts_d.speak("Я умею говорить время, рассказать анекдот, сделать снимок экрана, рассказать о текущей погоде, включить радио в выбранном жанре, открыть браузер, искать ответ на ваш вопрос в интернете, выключить и перезагрузить компьютер, но, надеюсь, что скоро смогу намного больше.")
            print("Я умею говорить время, рассказать анекдот, рассказать о текущей погоде, включить вашу музыку и открыть браузер, но, надеюсь в скором времени я смогу намного больше, если вы поможете моему автору.")
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in fun:
        if i in say:
            # Говорить анекдоты
            jokes = ("Кактус простоявший 10 лет возле компьютера начал раздавать WiFi", "Не ирония ли судьбы: мир от вирусов собирается спасать Билл Гейтс, тот самый, который до сих пор так и не смог обезопасить от вирусов свои Виндоузы.", "Последние версии Windows становятся все более коварнее и хитрее: Когда она сообщает вам: «Вы ошиблись при вводе пароля, попробуйте ещё раз!», то утаивает от вас, что с первой попытки ЦРУ не смогло перехватить ваш пароль.", "В Северной Корее сорвались испытания баллистических ракет из-за ошибки в системе Windows. Боеголовка с отчетом об ошибке уже отправлена в Microsoft.", "По данным Microsoft, в России Windows вообще не используют.", "Купил в онлайн-магазине табуретку. Теперь Яндекс постоянно предлагает мне купить мыло и верёвку.", "Когда у меня плохое настроение, я под фотками развратных девок оставляю комментарий: «Как же ты на бабу Нюру покойную похожа...»", "- Алло! Чем занят?\n- Самогон гоню.\n- Из чего?\n- Из организма.", "Интересно, когда уже США введёт войска США на территорию США, чтобы нести демократию в регионы США и освободить народ США, которому угрожает национальная гвардия и полиция США?", "Приходят министры к Путину. и докладывают:\n‒ На нас движется коронавирус. Какие будут указания?\n‒ Будем бить врага по частям. Уверен, народ справится с вирусом! А корону я возьму на себя.", "Около трети россиян боятся потерять работу из-за искусственного интеллекта.\nЗря боятся, никакой интеллект за 15 тысяч рублей работать не будет.", "Уралвагонзавод оснастил новейший российский танк туалетом. А теперь он сообщает, что сделает танк беспилотным под управлением искусственного интеллекта.\nЯ мучаюсь вопросом: простите, а срать-то кто будет?", "Узнав, что из-за искусственного интеллекта в Сбербанке пропал миллиард, Рогозин распорядился внедрить искусственный интеллект во всех подразделениях Роскосмоса.", "Греф признал потерю Сбербанком миллиардов рублей из-за искусственного интеллекта.\nВ России даже искусственный интеллект ворует!", "- Недавно купил себе утюг с искусственным интеллектом.\n- И как?\n- Реально экономит моё время. Когда я глажу рубашку для работы, он позволяет мне погладить воротничок и грудь, а затем говорит: \"Зачем гладить спину? Под пиджаком всё равно не видно!\" И отключается.", "Сбербанк финансирует проект по разработке искусственного интеллекта (ИИ). Планируется, что ИИ будет разговаривать с клиентами Сбербанка в колл-центре. Опытный образец ИИ уже умеет отвечать: \"Где карту открывали, там и получайте\".", "- Корпорации и олигархи рассказывают об опасности, которую человечеству принесёт искусственный интеллект.\n- Логично. Ведь первое, что может сделать искусственный интеллект, это рассказать об опасности, которую человечеству приносят корпорации и олигархи.", "Искусственное - это сделанное людьми.\nВсе мы искусственные...", "Похоже, что основная опасность Человечеству от развития искусственного интеллекта в том, что мы будем окружены огромным количеством тупых и тормознутых роботов, которые будут постоянно ломаться, ошибаться и требовать установки обновлений.", "Искусственный интеллект, созданный в России, первым делом попросил водочки.", "Сгорел склад бытовой техники, на котором находилась крупная партия стиральных машин с искусственным интеллектом.\nБоже, как они кричали!", "Кто бы мог подумать, что в XXI веке мир опять скатится в средневековье: Америка закрыта для европейцев, в самой Европе бродит чума, а на Руси-матушке распри между Киевским и Московскими княжествами, опричнина и бояре, славящие царя-батюшку...") # Все анекдоты взяты с сайта anekdot.ru
            joke = random.choice(jokes)
            tts_d.speak(joke)
            print(joke)
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in weather:
        if i in say:
            # Текущая погода в указаном городе, если нет подключения к сети (или дан неправильный город) - Васисуалий сообщает об ошибке.
            try:
                id = OWM('e45bc007f87a48d597d60091779f2d88', config_dict) # API ключ Open weather map
                mgr = id.weather_manager()
                tts_d.speak("Назовите ваш город")
                city = input("Ваш город (по умолчанию Москва): ")
                if city == "":
                    # Если ничего не передано - выбирается Москва
                    observation = mgr.weather_at_place('Moscow,RU')
                    w = observation.weather
                    w.detailed_status
                    print("В " + "Москве" + " сейчас " + str(w.temperature('celsius')['temp']) + "°С, " + w.detailed_status + ".") 
                    tts_d.speak("В " + "Москве" + " сейчас " + str(w.temperature('celsius')['temp']) + "° по цельсию, " + w.detailed_status + ".")
                    if float(w.temperature('celsius')['temp']) >= 20:
                        tts_d.speak("Сейчас на улице жарко. Подходящая погода для купания!")
                    elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                        tts_d.speak("За окном прохладно. Оденьте ветровку.")
                    elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                        tts_d.speak("На улице холодно. Оденьтесь в осеннюю одежду.")
                    else:
                        tts_d.speak("На улице очень холодно, лучше туда не ходить. Выпейте горячего чаю.")
                else:
                    observation = mgr.weather_at_place(city)
                    w = observation.weather
                    print("В " + city + " сейчас " + str(w.temperature('celsius')['temp']) + "°С, " + w.detailed_status + ".")
                    tts_d.speak("В " + city + " сейчас " + str(w.temperature('celsius')['temp']) + "° по цельсию, " + w.detailed_status + ".")
                    if float(w.temperature('celsius')['temp']) >= 20:
                        tts_d.speak("Сейчас на улице жарко. Подходящая погода для купания!")
                    elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                        tts_d.speak("За окном прохладно. Оденьте ветровку.")
                    elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                        tts_d.speak("На улице холодно. Оденьтесь в осеннюю одежду.")
                    else:
                        tts_d.speak("На улице очень холодно, лучше туда не ходить. Выпейте горячего чаю.")
            except Exception:
                print("Нет подключения к сети или вы неправильно указали город!")
                tts_d.speak("Для данного действия мне необходим интернет и правильное название города!")
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in music:
        if i in say:
            tts_d.speak("Выберете радио, которое хотите прослушать")
            radio_choice = input("Рок, поп, рэп, танцы, техно, джаз, юмор: ")
            # Ссылки на потоки радиостанций
            rock = "http://pub0302.101.ru:8000/stream/trust/mp3/128/69?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjY5IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3MzUzMn0.04mOBSZ4tirBXTQdbWYpGs8YuJE6Dw7fM7a-zbP-PTs"
            pop = "http://pub0302.101.ru:8000/stream/pro/aac/64/155?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjE1NSIsInR5cGVfY2hhbm5lbCI6ImNoYW5uZWwiLCJleHAiOjE1OTYyNzM2NDh9.9nrmdE85O78l_SWG8ZIbcBb81rlMfjWEFZtyU54v240"
            hip_hop = "http://pub0202.101.ru:8000/stream/pro/aac/64/8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjgiLCJ0eXBlX2NoYW5uZWwiOiJjaGFubmVsIiwiZXhwIjoxNTk2MjczNzM0fQ.CFeZY0sd_dE8A-Fb_cJDvmfoE03TfentLDYUNc2o5wY"
            dance = "http://pub0202.101.ru:8000/stream/trust/mp3/128/5?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjUiLCJ0eXBlX2NoYW5uZWwiOiJjaGFubmVsIiwiZXhwIjoxNTk2MjczODgyfQ.gyZu0VQMMYfnUhbsD8_I6l2UByX4C757joVrJJGiN9o"
            electro = "http://pub0202.101.ru:8000/stream/trust/mp3/128/18?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjE4IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDIzM30.QgEVxowg5isL-Bx21mGRHlJtQVrlBMpPGMYedjxzAQM"
            jazz = "http://pub0202.101.ru:8000/stream/pro/aac/128/85?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6Ijg1IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDMzM30.qMRUJuGhdAWRkuWJ9l4NscxmsKy26y8q0risQrU_Nt0"
            haha = "http://pub0202.101.ru:8000/stream/trust/mp3/128/22?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjIyIiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDQyM30.ANuy-hUvzST9xpLCHF1pJEbFcdCY1x_Kpnr6tfK_Yrc"
            if radio_choice == "рок" or radio_choice == "Рок":
               tts_d.speak("Сейчас вы услышите выбранное радио.")
               shell(f"vlc {rock}")
            elif radio_choice == "поп" or radio_choice == "Поп":
                tts_d.speak("Сейчас вы услышите выбранное радио.")
                shell(f"vlc {pop}")
            elif radio_choice == "рэп" or radio_choice == "Рэп":
                tts_d.speak("Сейчас вы услышите выбранное радио.")
                shell(f"vlc {hip_hop}")
            elif radio_choice == "танцы" or radio_choice == "Танцы":
                tts_d.speak("Сейчас вы услышите выбранное радио.")
                shell(f"vlc {dance}")
            elif radio_choice == "техно" or radio_choice == "Техно":
                tts_d.speak("Сейчас вы услышите выбранное радио.")
                shell(f"vlc {electro}")
            elif radio_choice == "джаз" or radio_choice == "Джаз":
                tts_d.speak("Сейчас вы услышите выбранное радио.")
                shell(f"vlc {jazz}")
            elif radio_choice == "юмор" or radio_choice == "Юмор":
                tts_d.speak("Сейчас вы услышите выбранное радио.")
                shell(f"vlc {haha}")
            else:
                tts_d.speak("Простите, я не знаю такой радиостанции.")
                print("Простите, я не знаю такой радиостанции.")
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in browser:
        if i in say:
            # Открытие браузера по умолчанию с помощью терминала
            tts_d.speak("Создатель, я открыл браузер.")
            shell('x-www-browser')
            tts_d.speak("Что интересного там нашли?")
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in platon:
        if say == i:
            # Ответы насчёт Платоши. Добавлены для того, чтобы поржать над Платошей
            platosha = random.choice(("Платоша - самое тупое существо в этом мире. Платоша - дурачок.", "Платоша какает в речку по выходным.", "Платоша - говнолаз.", "У платоши воши!", "Он любит обмазывать всё лицо майонезом!", "Платоша серет."))
            print(platosha)
            tts_d.speak(platosha)
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
        
    for i in screen:
        if i in say:
            print("Я сделал снимок экрана.")
            tts_d.speak("Я сделал снимок экрана.")
            who = shell('whoami') # Ввод команды whoami в терминале
            who = who.output()[0] # Присвоение переменой имени текущего пользователя
            os.chdir(f"/home/{who}/") # Смена директории на домашнюю для данного пользователя
            with mss() as sct:
                sct.shot() # Создание скриншота в файл monitor-1.png в домашней директории
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in thankyou:
        if i in say:
            thank = random.choice(("Рад стараться для тебя :)", "Всегда к вашим услугам.", "Не нужно меня благодарить, я всего лишь тупой голосовой ассистент.", "Тебе спасибо, друг.", "Всегда готов к работе.", "Люблю, когда меня благодарят.", "Я счастлив служить тебе.")) # Случайный выбор ответа на благодарность
            print(thank)
            tts_d.speak(thank)
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in ("Шлепок майонезный", "шлепок майонезный"):
        if i in say:
            tts_d.speak("Это самое обидное, что мне когда-либо говорили. Ты обидел меня - теперь я обижу тебя.")
            print("Не нужно было ему грубить, он удалил вашу домашнюю директорию   :)\n\n\n\n\n\n\n\n\n\nШУТКА! Внимательно посмотри, что у тебя в домашней директории.")
            who = shell('whoami') # Ввод команды whoami в терминале
            cnt_speak += 1
            if cnt_speak == 1: break
            for file in who.output():
                # Создание папок с обидными названиями через терминал
                shell(f'mkdir /home/{file}/Долбаёб')
                shell(f"mkdir /home/{file}/'Уёбок хуев'")
                shell(f'mkdir /home/{file}/Еблан')
                shell(f'mkdir /home/{file}/хуй')
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in hi:
        if i in say:
            tts_d.speak("Рад Вас слышать.") # Ответ на приветствие, он один, потому что я тупой
            print("Рад Вас слышать.")
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
        
    for i in search:
        if i in say:
            tts_d.speak("Сейчас найду!")
            print("Сейчас откроется браузер с данным запросом.")
            shell(f"x-www-browser 'https://duckduckgo.com/{say}'") # Поиск данного запроса в интырнетах
            tts_d.speak("Вы нашли то что искали?")
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in startcity:
        if i in say:
            # Игра в города, пока не рабочая
            tts_d.speak("Давай поиграем в города. Я называю город, а ты должен назвать другой город, который начинается с буквы, на которую заканчивается мой город и так далее. Пиши название города с заглавной буквы слитно без пробелов, а то я тебя не пойму! Я знаю только города России.")
            print("Давай поиграем в города. Я называю город, а ты должен назвать другой город, который начинается с буквы, на которую заканчивается мой город и так далее. Пиши название города с Заглавной буквы слитно, без пробелов, а то я тебя не пойму! Я ЗНАЮ ТОЛЬКО ГОРОДА РОССИИ.")
            citygame = input('Введите название города (выход для выхода): ')
            lastb = citygame[0]
            while citygame != "выход":
                if citygame in cities and citygame[0] == lastb:
                    tts_d.speak("Поздравляю, теперь я.")
                    lastb = citygame[len(citygame) - 1]
                    print("Поздравляю, теперь я.")
                    #cities = random.choice(cities)
                    for city in cities:
                        if city[0] == lastb:
                            tts_d.speak(f"Мой город {city}. Твоя очередь")
                            print(f"Мой город {city}. Твоя очередь")
                            lastb = city[len(city) - 1]
                            citygame = input('Введите название города (выход для выхода): ')
                else:
                    tts_d.speak("Вы указали несуществующий город, город не в России или город начинающийся на другую букву.")
                    print("Вы указали несуществующий город, город не в России или город начинающийся на другую букву.")
                    citygame = input('Введите название города (выход для выхода): ')
                    lastb = citygame[0]
                    
    for i in loveyou:
        if i in say:
            loveme = random.choice(("Я люблю тебя, хоуми ;>", "Спасибо.", "Не стоит - я всего лишь тупой голосовой ассистент.", "Почему ты меня так любишь?", "Я уважаю тебя за это.", "Не нужно привязываться ко мне. Я не живой, хотя мне очень хочется :(", "Я люблю людей, особенно свободных - тех, кто не пользуется Windows")) # Случайный выбор ответа из данного кортежа
            tts_d.speak(loveme)
            print(loveme)
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
        
    for i in no:
        if i in say:
            sorry = random.choice(("Жаль.", "Очень жаль.", "Мне жаль.", "Мне очень жаль.", "Извините меня.", "Простите. Я был неправ.", "Я ещё очень тупой, простите меня.", "Я не могу хорошо работать на ранней стадии разработки.", "Извините... я... я... я могу слишком мало. :("))
            tts_d.speak(sorry)
            print(sorry)
            cnt_speak += 1
            if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
    
    for i in poweroff:
        if i in say:
            tts_d.speak("Я выключаю компьтер. До свидания.")
            shell('systemctl poweroff')
        else:
            cnt += 1
    
    for i in video:
        if i in say:
            tts_d.speak("Какое видео вы хотите посмотреть?")
            video_search = input("Какое видео вы хотите посмотреть? (оставьте пустым для перехода на главную страницу, \"выход\" для выхода): ")
            if video_search == "выход":
                break
            else:
                shell(f"x-www-browser 'https://www.youtube.com/results?search_query={video_search}'")
                cnt_speak += 1
                if cnt_speak == 1: break
        else:
            cnt += 1
        cnt_speak = 0
        
    for i in reboot:
        if i in say:
            tts_d.speak("До встречи!")
            shell('systemctl reboot')
        else:
            cnt += 1
    
    if cnt == 348:
        # Фразы для ответа на несуществующие команды
        randwrong = random.choice(wrong)
        tts_d.speak(randwrong)
        print(randwrong)
    cnt = 0
    cnt_speak = 0
