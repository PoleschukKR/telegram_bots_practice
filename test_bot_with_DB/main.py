import telebot
import sqlite3#встроенная бд для python
from telebot import types
bot = telebot.TeleBot('7435283333:AAFpLMAmQFm-BKQ7KTvu96i39v9AJzFDXWE')
name = None

@bot.message_handler(commands=['start'])#обработчик команды start
def start(message):
    conn = sqlite3.connect('test_bot_with_DB.sql')#объект conn обращается к функ. connect (параметр - назв файла)
    cur = conn.cursor() # объект-курсор через который сможем выполнять разные команды
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    # метод execute позв. выполнять некоторые sql команды. Используем для созд. табл.
    conn.commit() # функция commit синхронизирует команды
    cur.close() # закрытие курсора и соединения с бд
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегестрируем. Введите имя!')
    bot.register_next_step_handler(message, user_name)# метод для вызова следующей функции


def user_name(message): # функция user_name
   global name
   name = message.text.strip()
   bot.send_message(message.chat.id, 'Введите пароль!')
   bot.register_next_step_handler(message, user_pass)  # метод для вызова следующей функции


def user_pass(message): # функция user_name
   password = message.text.strip()

   conn = sqlite3.connect('test_bot_with_DB.sql')  # объект conn обращается к функ. connect (параметр - назв файла)
   cur = conn.cursor()  # объект-курсор через который сможем выполнять разные команды

   cur.execute(f"INSERT INTO users (name, pass) VALUES ('%s','%s')" %(name, password))
   # метод execute позв. выполнять некоторые sql команды. Используем для созд. табл.
   conn.commit()  # функция commit синхронизирует команды
   cur.close()  # закрытие курсора и соединения с бд
   conn.close()
   markup = types.InlineKeyboardMarkup()
   markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='list'))
   bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('test_bot_with_DB.sql')  # объект conn обращается к функ. connect (параметр - назв файла)
    cur = conn.cursor()  # объект-курсор через который сможем выполнять разные команды

    cur.execute('SELECT * FROM users')
    # метод execute позв. выполнять некоторые sql команды. Используем для созд. табл.
    users = cur.fetchall()  # функция возвращает все найденные записи
    # здесь commit не нужен, тк используется для создания бд

    info = ''
    for el in users:
        info += f'`Имя: {el[1]}, пароль: {el[2]}\n'

    cur.close()  # закрытие курсора и соединения с бд, обновления, удаления
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)