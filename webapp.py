from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6223917234:AAG4lOarM-GxYpYlgqCP64D-Dw8cdmIwrRQ')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://raw.githack.com/KostaSkolznev/intmontage/main/index.html')))
    await message.answer('Привет, мой друг', reply_markup = markup)

executor.start_polling(dp)
