from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
import asyncio
from config import BOT_TOKEN, WEBAPP_URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    web_app = WebAppInfo(url=f"{WEBAPP_URL}/index.html")
    web_app_cart = WebAppInfo(url=f"{WEBAPP_URL}/cart.html")
    
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Открыть меню", web_app=web_app)],
            [KeyboardButton(text="🛒 Моя корзина", web_app=web_app_cart)],
            [KeyboardButton(text="ℹ️ Информация")],
            [KeyboardButton(text="💬 Связаться с нами")]
        ],
        resize_keyboard=True
    )

    await message.answer("Привет! Открывай меню 👇", reply_markup=kb)

@dp.message()
async def echo_message(message: types.Message):
    await message.answer("Я пока умею только показывать меню через кнопку /start 😊")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
