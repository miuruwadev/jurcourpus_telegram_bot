from aiogram import Router, Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lang.ru.bot import (
    START_STAGES, STAGES_MESSAGE, STAGES_BACK,
    STAGES_START1, STAGES_START1_ANSWER,
    STAGES_START2, STAGES_START2_ANSWER,
    STAGES_START3, STAGES_START3_ANSWER,
    STAGES_START4, STAGES_START4_ANSWER,
)
from keyboards.stages import stages, back
from states.stages import StagesSteps


def register_stages_handlers(dp: Dispatcher):
    router = Router()

    @router.message(F.text == START_STAGES)
    @router.message(StagesSteps.step2, F.text == STAGES_BACK)
    async def handle_stages_start_keyboard(message: Message, state: FSMContext):
        await message.answer(STAGES_MESSAGE, reply_markup=stages)
        await state.set_state(StagesSteps.step1)

    @router.message(StagesSteps.step1, F.text == STAGES_START1)
    async def handle_stages_start1(message: Message, state: FSMContext):
        await message.answer(STAGES_START1_ANSWER, reply_markup=back)
        await state.set_state(StagesSteps.step2)

    @router.message(StagesSteps.step1, F.text == STAGES_START2)
    async def handle_stages_start2(message: Message, state: FSMContext):
        await message.answer(STAGES_START2_ANSWER, reply_markup=back)
        await state.set_state(StagesSteps.step2)

    @router.message(StagesSteps.step1, F.text == STAGES_START3)
    async def handle_stages_start3(message: Message, state: FSMContext):
        await message.answer(STAGES_START3_ANSWER, reply_markup=back)
        await state.set_state(StagesSteps.step2)

    @router.message(StagesSteps.step1, F.text == STAGES_START4)
    async def handle_stages_start4(message: Message, state: FSMContext):
        await message.answer(STAGES_START4_ANSWER, reply_markup=back)
        await state.set_state(StagesSteps.step2)


    dp.include_router(router)