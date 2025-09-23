from aiogram import Router, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter
from lang.ru.bot import (
    START_STATUS, START_HOWTO, START_,
    HOWTO_QUE1, HOWTO_QUE2, HOWTO_QUE3,
    HOWTO_YES, HOWTO_NO,
    HOWTO_EDU1, HOWTO_EDU2, HOWTO_EDU3, HOWTO_EDU4, HOWTO_EDU5,
    HOWTO_RESULT, HOWTO_FAILED, STAGES_BACK
)
from keyboards.howto import simple_answer, education, howto
from states.howto import HowToSteps
from states.stages import StagesSteps


def register_howto_handlers(dp: Dispatcher):
    router = Router()

    @router.message(F.text == START_STATUS)
    @router.message(StagesSteps.step1, F.text == STAGES_BACK)
    async def handle_que1(message: Message):
        await message.answer(START_, reply_markup=howto)

    @router.message(F.text == START_HOWTO)
    async def handle_que1(message: Message, state: FSMContext):
        await message.answer(HOWTO_QUE1, reply_markup=simple_answer)
        await state.set_state(HowToSteps.step1)

    @router.message(HowToSteps.step1, F.text == HOWTO_YES)
    async def handle_que2(message: Message, state: FSMContext):
        await message.answer(HOWTO_QUE2, reply_markup=education, parse_mode="MarkdownV2")
        await state.set_state(HowToSteps.step2)

    @router.message(HowToSteps.step2, F.text.in_({
        HOWTO_EDU1,
        HOWTO_EDU2,
        HOWTO_EDU3,
        HOWTO_EDU4
    }))
    async def handle_que3(message: Message, state: FSMContext):
        await message.answer(HOWTO_QUE3, reply_markup=simple_answer)
        await state.set_state(HowToSteps.step3)

    @router.message(HowToSteps.step3, F.text == HOWTO_YES)
    async def handle_final(message: Message, state: FSMContext):
        await message.answer(HOWTO_RESULT, reply_markup=howto)
        await state.clear()


    @router.message(StateFilter([HowToSteps.step1,
                    HowToSteps.step2,
                    HowToSteps.step3]), F.text.in_({HOWTO_NO, HOWTO_EDU5, HOWTO_NO}))
    async def handle_failed(message: Message, state: FSMContext):
        await message.answer(HOWTO_FAILED, reply_markup=howto)
        await state.clear()

    dp.include_router(router)