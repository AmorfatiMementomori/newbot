import telebot
from telebot import types

bot = telebot.TeleBot('5965594627:AAEti2ajGscLQT7abYILlKM1i2frYT70lOk')

@bot.message_handler(commands=['websiti'])
def open_websiti(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://ua.sinoptik.ua"))
    bot.send_message(message.chat.id,"Отлично вот нопка-ссылка", parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('/websiti')
    btn2 = types.KeyboardButton('/start')
    markup.add(btn1, btn2)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЯ живоооой!)))"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

# RUN
bot.polling(none_stop=True)
