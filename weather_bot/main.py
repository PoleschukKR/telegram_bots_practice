import telebot
import requests
import json

bot = telebot.TeleBot('7365651741:AAEQRYwLazNRUZFfi3yExgMdf3h_T5QC8wg')
API = '591b7bb0aaba77459382e7e312a7eb5f' # API from weather map


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    #  библиотека requests позволяет отправлять запрос по определенном URL-адресу
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200: # выполняем проверку
        data = json.loads(res.text) #  обращаемся к модулю json, через к функции loads => res
        temp = data["main"]["temp"] #  выводим значение ключа temp
        bot.reply_to(message, f'Сейчас температура в городе {city}: {temp}')

        if temp < 10:
            image = 'Rainy.png'
        elif 10 < temp < 20:
            image = 'cloudy.png'
        else:
            image = 'Sunny.png'

        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)

    else:
        bot.reply_to(message, f'Город указан не верно!')


bot.polling(none_stop=True)