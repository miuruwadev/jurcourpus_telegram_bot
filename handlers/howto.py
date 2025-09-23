from aiogram import Router, Dispatcher, F
from aiogram.types import Message
from lang.ru.bot import START_HOWTO, HOWTO_MESSAGE

router = Router()


def register_howto_handlers(dp: Dispatcher):
    @router.message(F.text == START_HOWTO)
    async def handle_reply_keyboard(message: Message):
        await message.answer(HOWTO_MESSAGE)

    dp.include_router(router)