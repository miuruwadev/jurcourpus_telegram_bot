from aiogram import Router, Dispatcher, F
from aiogram.types import Message
from lang.ru.bot import START_STAGES, STAGES_MESSAGE

router = Router()


def register_stages_handlers(dp: Dispatcher):
    @router.message(F.text == START_STAGES)
    async def handle_reply_keyboard(message: Message):
        await message.answer(STAGES_MESSAGE)

    dp.include_router(router)