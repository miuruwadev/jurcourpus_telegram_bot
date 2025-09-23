from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lang.ru.bot import (
    START_HOWTO,
    START_STAGES,
    HOWTO_YES, HOWTO_NO,
    HOWTO_EDU1, HOWTO_EDU2, HOWTO_EDU3, HOWTO_EDU4
    )

howto = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=START_HOWTO),
        KeyboardButton(text=START_STAGES)
    ]],
    resize_keyboard=True
)

simple_answer = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=HOWTO_YES),
        KeyboardButton(text=HOWTO_NO)
    ]],
    resize_keyboard=True
)

education = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text=HOWTO_EDU1),
        KeyboardButton(text=HOWTO_EDU2),
        KeyboardButton(text=HOWTO_EDU3),
        KeyboardButton(text=HOWTO_EDU4),
    ]],
    resize_keyboard=True
)