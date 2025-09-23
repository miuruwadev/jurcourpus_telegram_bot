from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lang.ru.bot import START_HOWTO, START_STAGES

keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=START_HOWTO),
        KeyboardButton(text=START_STAGES)
    ]],
    resize_keyboard=True
)