import telebot
from telebot import types
import webbrowser #библиотека для работы с web
bot = telebot.TeleBot('7328877174:AAEy7L9gjufnFto2Ud_Gao6-ezuR_J7ASGs')


@bot.message_handler(commands=['start']) # создаем декоратор, с помощью которого при /start выполняются определенные действия
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт 💻') #создание 1 кнопки
    markup.row(btn1) # определяем для 1 кнопки место в первом ряду
    btn2 = types.KeyboardButton('Удалить последнее сообщение ❌')
    btn3 = types.KeyboardButton('Редактировать текущее сообщение 🛠')
    markup.row(btn2, btn3) # определяем место для кнопок 2,3 во втором ряду
    file = open('./first_step_in_IT_picture.jpg', 'rb') # открытие файла, ссылка на него
   # bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, это мой первый телеграм бот! Рад, что ты зашел :)', reply_markup=markup)
    bot.send_photo(message.chat.id, file, reply_markup=markup) #бот отправляет файл с указанным выше путем, предлагая кнопки
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт 💻':
        bot.send_message(message.chat.id, 'Website is open!')

    elif message.text == 'Удалить последнее сообщение ❌':
        bot.send_message(message.chat.id, 'Сообщение удалено!')

@bot.message_handler(commands=['site', 'website']) # декоратор, открывающий web-site
def site(message):
    webbrowser.open('https://github.com/PoleschukKR')


@bot.message_handler(commands=['main','hello', 'привет']) #декоратор, приветствующий пользователя
def main(message):
    if message.from_user.last_name == None:
        bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}, это мой первый телеграм бот! Рад, что ты зашел :)')
    else:
        bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name} {message.from_user.last_name}, это мой первый телеграм бот! Рад, что ты зашел :)')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<em><b>Help</b> <u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        if message.from_user.last_name == None:
            bot.send_message(message.chat.id,
                             f'Привет, {message.from_user.first_name}, это мой первый телеграм бот! Рад, что ты зашел :)')
        else:
            bot.send_message(message.chat.id,
                             f'Привет, {message.from_user.first_name} {message.from_user.last_name}, это мой первый телеграм бот! Рад, что ты зашел :)')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

    elif 'спасибо' in message.text.lower():
        bot.send_message(message.chat.id, 'Всегда пожалуйста, обращайтесь!')

    elif message.text.lower() == 'github':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/PoleschukKR'))
        markup.add(types.InlineKeyboardButton('Стереть текст', callback_data='delete'))#параметр, указывающий на вызов некоторой функции,
        markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit')) # которая будет отвечать за действие этой кнопки
        bot.reply_to(message, 'Вы хотите перейти на страницу GitHub?', reply_markup=markup)

    elif message.text.lower() == 'кнопка':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Кнопка 1', url='https://github.com/PoleschukKR')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton('Кнопка 2', callback_data='delete')
        btn3 = types.InlineKeyboardButton('Кнопка 3', callback_data='edit')
        markup.row(btn2, btn3)
        bot.reply_to(message, 'Тест рядов кнопок', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)# декоратор для обработки callback
def callback_message(callback): # сама функция
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1) # бот удал. пред. сооб
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



@bot.message_handler(content_types=['audio', 'photo']) #декоратор для ответа на фото/audio
def get_photo(message):
    bot.reply_to(message, 'Прекрасное фото!')





bot.polling(none_stop=True)#работа бота не приостанавливается после соверш. действ.

