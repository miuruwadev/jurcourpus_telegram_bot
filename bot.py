import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from handlers.start import register_start_handlers
from handlers.howto import register_howto_handlers
from handlers.stages import register_stages_handlers

from config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

async def main():
    register_start_handlers(dp)
    register_howto_handlers(dp)
    register_stages_handlers(dp)
    await dp.start_polling(bot)
