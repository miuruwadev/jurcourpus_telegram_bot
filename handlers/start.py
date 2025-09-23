from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram import types

from keyboards.start import keyboard
from lang.ru.bot import START_MESSAGE


def register_start_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def send_welcome(message: types.Message):
        await message.reply(START_MESSAGE, reply_markup=keyboard)