from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.webhook_info import WebhookInfo

bot = Bot('7406233136:AAEP7C6_SGmwTLt5Mh7lfW3iO5wwPXWHgVE')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebhookInfo(url='https://github.com/PoleschukKR')))
    await message.answer('Привет!', reply_markup=markup)

executor.start_polling(dp)