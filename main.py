import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TELEGRAM_BOT_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Hello world")

# Основная функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())