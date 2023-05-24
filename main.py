import telebot
from telebot import types
from random import randint
from config import host_c,user_c,password_c,db_name_c,port_c,token
import psycopg2
from datetime import datetime, timedelta
import calendar


bot = telebot.TeleBot(token)

conn = psycopg2.connect(host=host_c,
    user=user_c,
    password=password_c,
    database=db_name_c,
    port=port_c)
cursor = conn.cursor()


today = datetime.today() #сегодня
weekday_num = today.weekday() #день недели сегодня
delta_days = timedelta(days=weekday_num) # определяем дельту в днях от текущей даты до начала недели
start_of_week = today - delta_days # определяем дату начала недели
# start_of_week_formatted = start_of_week.strftime('%m-%d-%Y')

@bot.message_handler(commands=['start'])
def start(message):
    # keyboard.row("Хочу", "/help")

    keyboard = types.InlineKeyboardMarkup()
    key_d_1 = types.InlineKeyboardButton(text='Расписание на Понедельник', callback_data='d_1')
    key_d_2 = types.InlineKeyboardButton(text='Расписание на Вторник', callback_data='d_2')
    key_d_3 = types.InlineKeyboardButton(text='Расписание на Среду', callback_data='d_3')
    key_d_4 = types.InlineKeyboardButton(text='Расписание на Четверг', callback_data='d_4')
    key_d_5 = types.InlineKeyboardButton(text='Расписание на Пятницу', callback_data='d_5')
    key_d_6 = types.InlineKeyboardButton(text='Расписание на Субботу', callback_data='d_6')
    key_TW = types.InlineKeyboardButton(text='Расписание на эту неделю', callback_data='TW')
    key_NW = types.InlineKeyboardButton(text='Расписание на следующую неделю', callback_data='NW')

    keyboard.add(key_d_1)
    keyboard.add(key_d_2)
    keyboard.add(key_d_3)
    keyboard.add(key_d_4)
    keyboard.add(key_d_5)
    keyboard.add(key_d_6)
    keyboard.add(key_TW)
    keyboard.add(key_NW)

    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
    print(message.chat.id)

    

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    match call.data:
        case "TW":
            str_res_adw = ""
            day = start_of_week + timedelta(days=0)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Понедельник\n____________\n")
            day = start_of_week + timedelta(days=1)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Вторник\n____________\n")
            day = start_of_week + timedelta(days=2)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Среда\n____________\n")
            day = start_of_week + timedelta(days=3)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Четверг\n____________\n")
            day = start_of_week + timedelta(days=4)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Пятница\n____________\n")
            day = start_of_week + timedelta(days=5)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Суббота\n____________\n")
            bot.send_message(call.message.chat.id, "Информация о парах на эту неделю:" + "\n" + str_res_adw)
        case "NW":
            str_res_adw = ""
            day = start_of_week + timedelta(days=7)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Понедельник\n____________\n")
            day = start_of_week + timedelta(days=8)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Вторник\n____________\n")
            day = start_of_week + timedelta(days=9)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Среда\n____________\n")
            day = start_of_week + timedelta(days=10)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Четверг\n____________\n")
            day = start_of_week + timedelta(days=11)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Пятница\n____________\n")
            day = start_of_week + timedelta(days=12)
            day_sql = day.strftime('%Y-%m-%d')
            str_res_adw += get_day_info(day_sql, "Суббота\n____________\n")
            bot.send_message(call.message.chat.id, "Информация о парах на следующую неделю:" + "\n" + str_res_adw)
        case "d_1":
            bot.send_message(call.message.chat.id, "Информация о парах в понедельник:")
            day = start_of_week + timedelta(days=0)
            day_sql = day.strftime('%Y-%m-%d')
            bot.send_message(call.message.chat.id, get_day_info(day_sql, "Понедельник\n____________\n"))
        case "d_2":
            bot.send_message(call.message.chat.id, "Информация о парах во вторник:")
            day = start_of_week + timedelta(days=1)
            day_sql = day.strftime('%Y-%m-%d')
            bot.send_message(call.message.chat.id, get_day_info(day_sql, "Вторник\n____________\n"))
        case "d_3":
            bot.send_message(call.message.chat.id, "Информация о парах в среду:")
            day = start_of_week + timedelta(days=2)
            day_sql = day.strftime('%Y-%m-%d')
            bot.send_message(call.message.chat.id, get_day_info(day_sql, "Среда\n____________\n"))
        case "d_4":
            bot.send_message(call.message.chat.id, "Информация о парах в четверг:")
            day = start_of_week + timedelta(days=3)
            day_sql = day.strftime('%Y-%m-%d')
            bot.send_message(call.message.chat.id, get_day_info(day_sql, "Четверг\n____________\n"))
        case "d_5":
            bot.send_message(call.message.chat.id, "Информация о парах в пятницу:")
            day = start_of_week + timedelta(days=4)
            day_sql = day.strftime('%Y-%m-%d')
            bot.send_message(call.message.chat.id, get_day_info(day_sql, "Пятница\n____________\n"))
        case "d_6":
            bot.send_message(call.message.chat.id, "Информация о парах в субботу:")
            day = start_of_week + timedelta(days=5)
            day_sql = day.strftime('%Y-%m-%d')
            bot.send_message(call.message.chat.id, get_day_info(day_sql, "Суббота\n____________\n"))


def get_day_info(day, additional_data):
    cursor.execute(f"Select t.subject_name, t.room, t.start_time, ts.teacher_full_name FROM public.timetable as t Left Join public.teachers as ts ON ts.subject_name = t.subject_name WHERE day = '{day}' ORDER BY t.start_time ASC")
    records = list(cursor.fetchall())
    # return(str(records))
    str_res = additional_data
    for x in records:
        str_res += x[0] + " " + x[1] + " " + str(x[2])[0:5] + " " + x[3].split()[0] +" "+ x[3].split()[1][0].upper() +"."+ x[3].split()[2][0].upper()  +".\n"
    return str(str_res + "\n____________________________________\n")
    # return(f"Select t.subject_name, t.room, t.start_time, ts.teacher_full_name FROM public.timetable as t Left Join public.teachers as ts ON ts.subject_name = t.subject_name WHERE day = '{day}'")


def get_week_num():
    day = int(datetime.now().day)
    month = int(datetime.now().month)
    year = int(datetime.now().year)
    calendar_ = calendar.TextCalendar(calendar.MONDAY)
    lines = calendar_.formatmonth(year, month).split('\n')
    days_by_week = [week.lstrip().split() for week in lines[2:]]
    str_day = str(day)
    for index, week in enumerate(days_by_week):
        if str_day in week:
            return index + 1
    raise ValueError(
        f'Нет дня {day} в месяце с номером {month} в {year} году')


def get_week_grade(next=False):
    if next == True:
        n = 0
    else:
        n = 1
    if get_week_num() % 2 == n:
        return 'down'
    else:
        return 'up'


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(
        message.chat.id, 'официальный сайт МТУСИ - https://mtuci.ru/!')


@bot.message_handler(commands=['week'])
def week(message):
    week = get_week_grade()
    if week == 'up':
        answer = 'верхняя (нечётная)'
    else:
        answer = 'нижняя (чётная)'
    answer = 'Сейчас ' + answer + ' неделя'
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, """
    /start - начать работу бота, вывести список команд
    /help - помощь
    /week - верхняя или нижняя неделя?
    /mtuci - официальный сайт МТУСИ
    """)


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, 'Вы можете воспользоваться командой /help чтобы узнать функции бота, либо /start чтобы получить актуальную информацию по расписанию занятий')

bot.infinity_polling()
