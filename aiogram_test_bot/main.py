
from aiogram import Bot, Dispatcher, executor, types
# class Bot для подключения бота, Dispatcher для работы с ботом/ отслеживания сообщений
# executor постоянного выполнения

bot = Bot('7333376346:AAERXwaiVTPXW_UDjDOZM2SnftlfUzh5jlQ')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) # декоратор для отслеживания команды
async def start(message: types.message):  # любая func в aiogram асинхронна, добавляем тип параметра
    # await bot.send_message(message.chat.id, 'Hello')   "ожидаем от бота выполнения"
    await message.answer('Hello')  # Используем для отправки сообщения без chat.id
    # await message.reply('Hi') для ответа на конкретное сообщение

    # file = open('/some.png', 'rb') для ответа на фото
    # await message.answer_photo(file)


@dp.message_handler(commands=['inline'])
async def info(message: types.message):
    markup = types.InlineKeyboardMarkup()  # при желании row_width
    markup.add(types.InlineKeyboardButton('Site', url='https://itproger.com'))  # для добавления кнопки
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello, dear friend!', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # кнопки показываются 1 раз
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Library'))
    await message.answer('Hello, my dear friend!', reply_markup=markup)

executor.start_polling(dp)  # для непрерывной работы бота
