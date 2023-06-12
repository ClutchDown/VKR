import telebot
from telebot import types
from telebot import util
import logging
import os
from datetime import datetime
import yadisk
from threading import Timer
import sqlite3

y = yadisk.YaDisk(token="y0_AgAAAAAhWBnHAAoAegAAAADkmGVRV9ACKItuQsea2XTWtXnm6RRnFLQ")
bot = telebot.TeleBot('6254567985:AAGoeKTBbH2AZ8PDTj-80f3uvCZimXAoXGY', skip_pending=True)

def run( ):
    path = r'C:\Users\VictorPC\Desktop\8 семестр учеба\диплом\bot\logs'
    date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
    y.mkdir(f'/logging/{date}')

    for address, dirs, files in os.walk(path):
        for dir in dirs:
            y.mkdir(f'/logging/{date}/{dir}')
            print(f'Папка {dir} создана')
        for file in files:
            print(f'Файл {file} загружен')
            y.upload(f'{address}/{file}', f'/logging/{date}/{file}')
    Timer(2000.0, run).start()
run()



@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS logins_id(
                id INTEGER
                )""")
    connect.commit()
    guy_id = message.chat.id
    cursor.execute(f"SELECT id FROM logins_id WHERE id = {guy_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO logins_id VALUES(?);", user_id)
        connect.commit()
    nameOfUser = f'Здравствуй, {message.from_user.first_name}'
    bot.send_message(message.chat.id, nameOfUser, parse_mode='html')
    photo = open('Greeting-Emoji-PNG-Transparent.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('start.txt.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    bachelor = types.KeyboardButton('/Бакалавриат')
    master = types.KeyboardButton('/Магистратура')
    keyboard_markup.add(bachelor, master)
    bot.send_message(message.chat.id, 'Выбери куда хотите поступить', reply_markup=keyboard_markup)




@bot.message_handler(commands=['home'])
def home(message):
    bot.send_message(message.chat.id, 'Вы на стартовой странице. Вы можете снова выбрать что именно вас интересует с помощью кнопок или с помощью подсказки слева')
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    bachelor = types.KeyboardButton('/Бакалавриат')
    master = types.KeyboardButton('/Магистратура')
    keyboard_markup.add(bachelor, master)
    bot.send_message(message.chat.id, 'Выбор за вами', reply_markup=keyboard_markup)

@bot.message_handler(commands=['admission'])
def admission(message):
    photo = open('priemka.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('admission.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)
    keyboard = types.InlineKeyboardMarkup()
    url = types.InlineKeyboardButton(text='*Клик*', url='https://www.nstu.ru/entrance/enrollment_campaign')
    keyboard.add(url)
    bot.send_message(message.chat.id, 'Ссылка на приёмную кампанию', reply_markup=keyboard)

##@bot.message_handler(content_types=['text'])
#def idk(message):
 #   bot.send_message(message.chat.id, 'К сожалению, я не могу распознать текст. Пожалуйста, выберите необходимую вам информацию в всплывающем меню')

@bot.message_handler(commands=['Назад'])
def home(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    avtf = types.KeyboardButton('/АВТФ')
    mtf = types.KeyboardButton('/МТФ')
    fma = types.KeyboardButton('/ФМА')
    fpmi = types.KeyboardButton('/ФПМИ')
    ref = types.KeyboardButton('/РЭФ')
    ftf = types.KeyboardButton('/ФТФ')
    fen = types.KeyboardButton('/ФЭН')
    fb = types.KeyboardButton('/ФБ')
    fgo = types.KeyboardButton('/ФГО')
    ist = types.KeyboardButton('/ИСТ')
    home = types.KeyboardButton('/home')
    keyboard_markup.add(avtf, mtf, fpmi, ref, ftf, fen, fb, fgo, ist, fma, home)
    bot.send_message(message.chat.id, 'Попробуйте еще раз выбрать факультет', reply_markup=keyboard_markup)

@bot.message_handler(commands=['Hазад'])
def home(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    avtf = types.KeyboardButton('/АВТФм')
    mtf = types.KeyboardButton('/МТФм')
    fma = types.KeyboardButton('/ФМАм')
    fpmi = types.KeyboardButton('/ФПМИм')
    ref = types.KeyboardButton('/РЭФм')
    ftf = types.KeyboardButton('/ФТФм')
    fen = types.KeyboardButton('/ФЭНм')
    fb = types.KeyboardButton('/ФБм')
    fgo = types.KeyboardButton('/ФГОм')
    ist = types.KeyboardButton('/ИСТм')
    home = types.KeyboardButton('/home')
    keyboard_markup.add(avtf, mtf, fpmi, ref, ftf, fen, fb, fgo, ist, home)
    bot.send_message(message.chat.id, 'Выбери интересующий фалькутет', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Бакалавриат"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    avtf = types.KeyboardButton('/АВТФ')
    mtf = types.KeyboardButton('/МТФ')
    fma = types.KeyboardButton('/ФМА')
    fpmi = types.KeyboardButton('/ФПМИ')
    ref = types.KeyboardButton('/РЭФ')
    ftf = types.KeyboardButton('/ФТФ')
    fen = types.KeyboardButton('/ФЭН')
    fb = types.KeyboardButton('/ФБ')
    fgo = types.KeyboardButton('/ФГО')
    ist = types.KeyboardButton('/ИСТ')
    home = types.KeyboardButton('/home')
    keyboard_markup.add(avtf, mtf, fpmi, ref, ftf, fen, fb, fgo, ist, fma, home)
    bot.send_message(message.chat.id, 'Выбери интересующий фалькутет', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Магистратура"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    avtf = types.KeyboardButton('/АВТФм')
    mtf = types.KeyboardButton('/МТФм')
    fma = types.KeyboardButton('/ФМАм')
    fpmi = types.KeyboardButton('/ФПМИм')
    ref = types.KeyboardButton('/РЭФм')
    ftf = types.KeyboardButton('/ФТФм')
    fen = types.KeyboardButton('/ФЭНм')
    fb = types.KeyboardButton('/ФБм')
    fgo = types.KeyboardButton('/ФГОм')
    ist = types.KeyboardButton('/ИСТм')
    home = types.KeyboardButton('/home')
    keyboard_markup.add(avtf, mtf, fpmi, ref, ftf, fen, fb, fgo, ist, home)
    bot.send_message(message.chat.id, 'Выбери интересующий фалькутет', reply_markup=keyboard_markup)

@bot.message_handler(commands=["АВТФ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    inf_technic = types.KeyboardButton('/Информатика_и_вычислительная_техника')
    inf_tec = types.KeyboardButton('/Информационные_системы_и_технологии')
    inf = types.KeyboardButton('/Прикладная_информатика')
    program = types.KeyboardButton('/Программная_инженерия')
    device = types.KeyboardButton('/Приборостроение')
    bio = types.KeyboardButton('/Биотехнические_системы_и_технологии')
    manage_tech = types.KeyboardButton('/Управление_в_технических_системах')
    auto_sec = types.KeyboardButton('/Инф_безопасность_автоматизированных_систем')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(auto_sec,manage_tech, bio, device, program, inf, inf_tec, inf_tec, inf_technic, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Информатика_и_вычислительная_техника"])
def inf_technic(message):
    photo = open('inf_technic.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('inf_technic.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Информационные_системы_и_технологии"])
def inf_tec(message):
    large_text = open('inf_tec.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Прикладная_информатика"])
def inf(message):
    photo = open('inf_technic.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('inf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Программная_инженерия"])
def program(message):
    large_text = open('inf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Приборостроение"])
def device(message):
    photo = open('ZI.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('device.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Биотехнические_системы_и_технологии"])
def bio(message):
    large_text = open('device.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Управление_в_технических_системах"])
def manage_tech(message):
    photo = open('inf_technic.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('manage_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Инф_безопасность_автоматизированных_систем"])
def auto_sec(message):
    photo = open('ZI.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('auto_sec.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["МТФ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    tech_mach = types.KeyboardButton('/Технологические_машины_и_оборудование')
    auto_tech = types.KeyboardButton('/Автоматизация_тех_процессов_и_производств')
    constr_tech = types.KeyboardButton('/Конструкторско-тех_обеспечение_машиностроительных_производств')
    chem_tech = types.KeyboardButton('/Химическая_технология')
    mater_tech = types.KeyboardButton('/Материаловедение_и_технологии_материалов')
    start_auto = types.KeyboardButton('/Эксплуатация_транспортно-технологических_машин_и_комплексов')
    nano_eng = types.KeyboardButton('/Наноинженерия')
    tech_hud = types.KeyboardButton('/Технология_художественной_обработки_материалов')
    mech_rob = types.KeyboardButton('/Мехатроника_и_робототехника')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(tech_mach,auto_tech, chem_tech,mater_tech, start_auto, nano_eng, tech_hud, constr_tech, mech_rob, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Технологические_машины_и_оборудование"])
def tech_mach(message):
    photo = open('ptm.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('tech_mach.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Автоматизация_тех_процессов_и_производств"])
def auto_tech(message):
    photo = open('ptm.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('auto_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Конструкторско-тех_обеспечение_машиностроительных_производств"])
def constr_tech(message):
    large_text = open('constr_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Автоматизация_тех_процессов_и_производств"])
def chem_tech(message):
    large_text = open('chem_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Материаловедение_и_технологии_материалов"])
def mater_tech(message):
    photo = open('mater_tech.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mater_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Эксплуатация_транспортно-технологических_машин_и_комплексов"])
def start_auto(message):
    large_text = open('start_auto.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Наноинженерия"])
def nano_eng(message):
    photo = open('mater_tech.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('nano_eng.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Технология_художественной_обработки_материалов"])
def tech_hud(message):
    photo = open('mater_tech.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('tech_hud.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Мехатроника_и_робототехника"])
def mech_rob(message):
    photo = open('ptm.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mech_rob.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Химическая_технология"])
def chem_tech(message):
    large_text = open('chem_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФМА"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    el_el = types.KeyboardButton('/Электроэнергетика_и_электротехника')
    auto_tech_pr = types.KeyboardButton('/Автоматизация_тех_процессов_и_производств')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(el_el, auto_tech_pr, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Электроэнергетика_и_электротехника"])
def el_el(message):
    large_text = open('el_el.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Автоматизация_тех_процессов_и_производств"])
def el_el(message):
    large_text = open('auto_tech_pr.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФПМИ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    math_inf = types.KeyboardButton('/Прикладная_математика_и_информатика')
    math_softw = types.KeyboardButton('/Математическое_обеспечение_и_адм_инф_систем')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(math_inf, math_softw, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Прикладная_математика_и_информатика"])
def math_inf(message):
    large_text = open('math_inf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Математическое_обеспечение_и_адм_инф_систем"])
def math_softw(message):
    large_text = open('math_softw.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["РЭФ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    radio = types.KeyboardButton('/Радиотехника')
    inf_tech_tel = types.KeyboardButton('/Инфокомм_технологии_и_системы_связи')
    constr_tech_el = types.KeyboardButton('/Конструирование_и_технология_эл_средств')
    el_nanoel = types.KeyboardButton('/Электроника_и_наноэлектроника')
    nano_tech = types.KeyboardButton('/Нанотехнологии_и_микросистемная_техника')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(radio, inf_tech_tel, constr_tech_el, el_nanoel, nano_tech, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Радиотехника"])
def radio(message):
    large_text = open('radio.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Инфокомм_технологии_и_системы_связи"])
def inf_tech_tel(message):
    photo = open('TOR.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('inf_tech_tel.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Конструирование_и_технология_эл_средств"])
def constr_tech_el(message):
    photo = open('KTRS.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('constr_tech_el.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Электроника_и_наноэлектроника"])
def el_nanoel(message):
    photo = open('PPIME.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('el_nanoel.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Нанотехнологии_и_микросистемная_техника"])
def nano_tech(message):
    photo = open('PPIME.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('nano_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФТФ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    phisics = types.KeyboardButton('/Физика')
    foto_opto = types.KeyboardButton('/Фотоника_и_оптоинформатика')
    laser_tech = types.KeyboardButton('/Лазерная_техника_и_лазерные_технологии')
    tech_fiz = types.KeyboardButton('/Техническая_физика')
    kino = types.KeyboardButton('/Кинооператорство')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(phisics, foto_opto,laser_tech, tech_fiz, kino, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Физика"])
def phisics(message):
    large_text = open('phisics.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Фотоника_и_оптоинформатика"])
def foto_opto(message):
    large_text = open('foto_opto.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Лазерная_техника_и_лазерные_технологии"])
def laser_tech(message):
    large_text = open('laser_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Техническая_физика"])
def tech_fiz(message):
    large_text = open('laser_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Кинооператорство"])
def kino(message):
    large_text = open('kino.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФЭН"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    teplo_teplo = types.KeyboardButton('/Теплоэнергетика_и_теплотехника')
    electro_el = types.KeyboardButton('/Электроэнергетика_и_электротехника')
    techno_sfer = types.KeyboardButton('/Техносферная_безопасность')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(teplo_teplo, electro_el, techno_sfer, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Теплоэнергетика_и_теплотехника"])
def teplo_teplo(message):
    large_text = open('teplo_teplo.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Электроэнергетика_и_электротехника"])
def electro_el(message):
    photo = open('ELS.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('electro_el.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Техносферная_безопасность"])
def techno_sfer(message):
    photo = open('BT.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('techno_sfer.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФБ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    tech_prod = types.KeyboardButton('/Тех_продукции_и_организация_общественного_питания')
    economy = types.KeyboardButton('/Экономика')
    management = types.KeyboardButton('/Менеджмент')
    bisuness_inf = types.KeyboardButton('/Бизнес-информатика')
    eco_safety = types.KeyboardButton('/Экономическая_безопасность')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(tech_prod,economy, management, bisuness_inf, eco_safety, back)
    bot.send_message(message.chat.id, 'Выбери интересующий фалькутет', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Тех_продукции_и_организация_общественного_питания"])
def tech_prod(message):
    large_text = open('tech_prod.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Экономика"])
def economy(message):
    large_text = open('techno_sfer.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Менеджмент"])
def management(message):
    photo = open('MIS.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('management.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Бизнес-информатика"])
def bisuness_inf(message):
    large_text = open('bisuness_inf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Экономическая_безопасность"])
def eco_safety(message):
    large_text = open('eco_safety.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФГО"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    psycho = types.KeyboardButton('/Психология')
    social = types.KeyboardButton('/Социология')
    import_reg = types.KeyboardButton('/Зарубежное_регионоведение')
    philosofy = types.KeyboardButton('/Филология')
    lingv = types.KeyboardButton('/Лингвистика')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(psycho,social, import_reg,philosofy, lingv, back)
    bot.send_message(message.chat.id, 'Выбери интересующий фалькутет', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Психология"])
def psycho(message):
    photo = open('PIP.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('psycho.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Социология"])
def social(message):
    large_text = open('social.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Зарубежное_регионоведение"])
def import_reg(message):
    large_text = open('import_reg.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Филология"])
def philosofy(message):
    large_text = open('philosofy.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Лингвистика"])
def lingv(message):
    photo = open('IYA.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('lingv.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ИСТ"])
def bachelor_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    konfl = types.KeyboardButton('/Конфликтология')
    social_work = types.KeyboardButton('/Социальная_работа')
    yurist = types.KeyboardButton('/Юриспруденция')
    back = types.KeyboardButton('/Назад')
    keyboard_markup.add(konfl, social_work, yurist, back)
    bot.send_message(message.chat.id, 'Выбери интересующий фалькутет', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Конфликтология"])
def konfl(message):
    photo = open('CPCA.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('konfl.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Социальная_работа"])
def social_work(message):
    photo = open('CPCA.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('social_work.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Юриспруденция"])
def yurist(message):
    photo = open('logo_105_1650444077.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('yurist.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["АВТФм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    minf_technic = types.KeyboardButton('/Информатика_и_вычислительная_техника_М')
    minf = types.KeyboardButton('/Прикладная_информатика_М')
    mprogram = types.KeyboardButton('/Программная_инженерия_М')
    mdevice = types.KeyboardButton('/Приборостроение_М')
    mbio = types.KeyboardButton('/Биотехнические_системы_и_технологии_М')
    mmanage_tech = types.KeyboardButton('/Управление_в_технических_системах_М')
    mauto_sec = types.KeyboardButton('/Инф_безопасность_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(minf_technic,minf, mprogram,mdevice, mbio, mmanage_tech, mauto_sec, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Информатика_и_вычислительная_техника_М"])
def minf_technic(message):
    photo = open('inf_technic.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('minf_technic.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Прикладная_информатика_М"])
def minf(message):
    photo = open('inf_technic.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('minf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Программная_инженерия_М"])
def mprogram(message):
    large_text = open('mprogram.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Приборостроение_М"])
def mdevice(message):
    photo = open('ZI.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mdevice.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Биотехнические_системы_и_технологии_М"])
def mbio(message):
    large_text = open('mbio.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Управление_в_технических_системах_М"])
def mmanage_tech(message):
    photo = open('inf_technic.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mmanage_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Инф_безопасность_М"])
def mauto_sec(message):
    photo = open('ZI.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mauto_sec.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["МТФм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mconst = types.KeyboardButton('/Констр-тех_обеспечение_машиностроительных_произв_М')
    mchemistry = types.KeyboardButton('/Химическая_технология_М')
    mmaterial = types.KeyboardButton('/Материаловедение_и_технологии_материалов_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mconst,mchemistry, mmaterial, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Констр-тех_обеспечение_машиностроительных_произв_М"])
def mconst(message):
    photo = open('ptm.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mconst.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Химическая_технология_М"])
def mchemistry(message):
    large_text = open('mchemistry.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Материаловедение_и_технологии_материалов_М"])
def mmaterial(message):
    photo = open('mater_tech.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mconst.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФПМИм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mmath_inf = types.KeyboardButton('/Прикладная_математика_и_информатика_М')
    mmath_inf_adm = types.KeyboardButton('/Матем_обеспечение_и_адм_инфор_систем_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mmath_inf, mmath_inf_adm, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Прикладная_математика_и_информатика_М"])
def mmaterial(message):
    large_text = open('mmath_inf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Матем_обеспечение_и_адм_инфор_систем_М"])
def mmath_inf_adm(message):
    large_text = open('mmath_inf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["РЭФм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mradio = types.KeyboardButton('/Радиотехника_М')
    minf_tech_sys = types.KeyboardButton('/Инфокомм_технологии_и_системы_связи_М')
    mconst_tech = types.KeyboardButton('/Констр_и_технология_электронных_средств_М')
    mel_nanoel = types.KeyboardButton('/Электроника_и_наноэлектроника_М')
    mnano_micro = types.KeyboardButton('/Нанотехнологии_и_микросистемная_техника_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mradio,minf_tech_sys,mconst_tech, mel_nanoel, mnano_micro, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Радиотехника_М"])
def mradio(message):
    large_text = open('mradio.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Инфокомм_технологии_и_системы_связи_М"])
def minf_tech_sys(message):
    photo = open('KTRS.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('minf_tech_sys.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Констр_и_технология_электронных_средств_М"])
def mconst_tech(message):
    photo = open('KTRS.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mconst_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["Электроника_и_наноэлектроника_М"])
def mel_nanoel(message):
    photo = open('PPIME.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mel_nanoel.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Нанотехнологии_и_микросистемная_техника_М"])
def mnano_micro(message):
    photo = open('PPIME.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mnano_micro.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФТФм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mphis = types.KeyboardButton('/Физика_М')
    mradioftf = types.KeyboardButton('/Радиотехника_М')
    mopto = types.KeyboardButton('/Оптотехника_М')
    mtech_phis = types.KeyboardButton('/Техническая_физика_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mphis,mradioftf, mopto, mtech_phis, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Физика_М"])
def mphis(message):
    large_text = open('mphis.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Радиотехника_М"])
def mradioftf(message):
    large_text = open('mradioftf.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Оптотехника_М"])
def mopto(message):
    large_text = open('mopto.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Техническая_физика_М"])
def mtech_phis(message):
    large_text = open('mtech_phis.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФЭНм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mteplo = types.KeyboardButton('/Теплоэнергетика_и_теплотехника_М')
    mel_el = types.KeyboardButton('/Электроэнергетика_и_электротехника_М')
    mtech_sec = types.KeyboardButton('/Техносферная_безопасность_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mteplo, mel_el, mtech_sec, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Теплоэнергетика_и_теплотехника_М"])
def mteplo(message):
    large_text = open('mteplo.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Электроэнергетика_и_электротехника_М"])
def mel_el(message):
    large_text = open('mel_el.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Техносферная_безопасность_М"])
def mtech_sec(message):
    photo = open('BT.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mel_el.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФБм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mtech_org = types.KeyboardButton('/Технология_продукции_и_организация_общ_питания_М')
    meco = types.KeyboardButton('/Экономика_М')
    mmanagement = types.KeyboardButton('/Менеджмент_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mtech_org, meco, mmanagement, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Технология_продукции_и_организация_общ_питания_М"])
def mtech_org(message):
    large_text = open('mtech_org.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Экономика_М"])
def meco(message):
    large_text = open('meco.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Менеджмент_М"])
def mmanagement(message):
    photo = open('MIS.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mmanagement.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФГОм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mpsycho = types.KeyboardButton('/Психология_М')
    msocial = types.KeyboardButton('/Социология_М')
    mimport_reg = types.KeyboardButton('/Зарубежное_регионоведение_М')
    mmped_grad = types.KeyboardButton('/Педагогическое_образование_М')
    mpfilology = types.KeyboardButton('/Филология_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mpsycho, msocial, mimport_reg,mmped_grad, mpfilology, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Менеджмент_М"])
def mpsycho(message):
    photo = open('PIP.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mmmpsycho.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Социология_М"])
def msocial(message):
    large_text = open('msocial.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Зарубежное_регионоведение_М"])
def mimport_reg(message):
    large_text = open('mimport_reg.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Педагогическое_образование_М"])
def mmped_grad(message):
    photo = open('IYA.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('mmped_grad.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Филология_М"])
def mpfilology(message):
    large_text = open('mpfilology.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ИСТм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    msoc_work = types.KeyboardButton('/Социальная_работа_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(msoc_work, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Социальная_работа_М"])
def msoc_work(message):
    photo = open('CPCA.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('msoc_work.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["ФМАм"])
def master_degree(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    mel_el_fma = types.KeyboardButton('/Электроэнергетика_и_электротехника_М')
    mauto_process = types.KeyboardButton('/Автоматизация_тех_процессов_и_производств_М')
    mmanagement_tech = types.KeyboardButton('/Управление_в_технических_системах_М')
    back = types.KeyboardButton('/Hазад')
    keyboard_markup.add(mel_el_fma, mauto_process, mmanagement_tech, back)
    bot.send_message(message.chat.id, 'Выбери интересующее направление', reply_markup=keyboard_markup)

@bot.message_handler(commands=["Электроэнергетика_и_электротехника_М"])
def mel_el_fma(message):
    large_text = open('mel_el_fma.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Автоматизация_тех_процессов_и_производств_М"])
def mauto_process(message):
    large_text = open('mauto_process.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Управление_в_технических_системах_М"])
def mmanagement_tech(message):
    large_text = open('mmanagement_tech.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['nstu'])
def start(message):
    photo = open('nstuPhoto.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    large_text = open('about_nstu.txt', 'rb').read()
    splitted_text = util.smart_split(large_text)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)
    photo2 = open('nstu_old.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)





logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='./logs/logsNEW.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%D:%H:%M:%S',
                    level=logging.DEBUG)



bot.polling(none_stop=True)
