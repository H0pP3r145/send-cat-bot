from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = "5165419393:AAGHwHOCI4-W29yn02NosA5lUhPn4Q4ZY5Y"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
key = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Получить котика 🐱"))

def getCat():
    try:
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
    except:
        url = getCat()
    return url


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Приветствую тебя в боте, который посвящен одной красотке!\nПри нажатии на кнопку ниже бот отправит вам котика 😇", reply_markup=key)

@dp.message_handler(text = "Получить котика 🐱")
async def send_cat(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=getCat() ,caption="Вот твой котик)", reply_markup=key)   


executor.start_polling(dp, skip_updates=True)
