
import telebot
from telebot import types
from telebot import util

bot = telebot.TeleBot('6254567985:AAGoeKTBbH2AZ8PDTj-80f3uvCZimXAoXGY', skip_pending=True)
@bot.message_handler(commands=['home'])
def home(message):
    bot.send_message(message.chat.id, 'Вы на стартовой странице. Вы можете снова выбрать что именно вас интересует с помощью кнопок или с помощью подсказки слево')
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    bachelor = types.KeyboardButton('/Бакалавриат')
    master = types.KeyboardButton('/Магистратура')
    keyboard_markup.add(bachelor, master)
    bot.send_message(message.chat.id, 'Выбор за вами', reply_markup=keyboard_markup)

@bot.message_handler(commands=['admission'])
def start(message):
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