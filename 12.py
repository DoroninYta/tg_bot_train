import requests
import time

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


    
API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "6864297599:AAHGQDRqB3z9-5VP2R07GBRWhjg_rF2Ai38"
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
cat_resp : requests.Response

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

counter = 0
MAX_NUM = 100
offset = -2
timeout = -15
updates: dict


@dp.message(Command(commands = ["start"]))
async def start_command(message : Message):
    await message.answer("salam popolam, send me sth, and i will reply you same text")

@dp.message(Command(commands = ["help"]))
async def help_command(message : Message):
    await message.answer("print me something, i will resend you same")

@dp.message()
async def send_command(message : Message):
    await message.reply(text = message.text)
    print(message)


if __name__ == "__main__":
    dp.run_polling(bot)
                         

