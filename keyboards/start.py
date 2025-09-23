from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lang.ru.bot import START_STATUS

keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=START_STATUS),
    ]],
    resize_keyboard=True
)