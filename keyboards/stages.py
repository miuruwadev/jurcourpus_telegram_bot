from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lang.ru.bot import (
    STAGES_START1, STAGES_START2, STAGES_START3, STAGES_START4, STAGES_BACK
    )

stages = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=STAGES_START1)],
        [KeyboardButton(text=STAGES_START2)],
        [KeyboardButton(text=STAGES_START3)],
        [KeyboardButton(text=STAGES_START4)],
        [KeyboardButton(text=STAGES_BACK)],
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=STAGES_BACK),
    ]],
    resize_keyboard=True
)