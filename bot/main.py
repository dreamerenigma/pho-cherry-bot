import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from config import BOT_TOKEN, WEBAPP_URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    web_app = WebAppInfo(url=f"{WEBAPP_URL}/index.html")
    web_app_cart = WebAppInfo(url=f"{WEBAPP_URL}/cart.html")
    
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Открыть меню", web_app=web_app)],
            [KeyboardButton(text="🛒 Моя корзина", web_app=web_app_cart)],
            [KeyboardButton(text="ℹ️ Информация", web_app=None)],
            [KeyboardButton(text="💬 Связаться с нами")]
        ],
        resize_keyboard=True
    )

    await message.answer("Привет! Открывай меню 👇", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
