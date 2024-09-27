from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _

from button_name import region_button
from evos import stepState

vacancy_router = Router()


@vacancy_router.message((F.text == __("💼  Vacancies")) | (F.text == "💼  Bo'sh ish o'rin"))
async def vacancies_handler(message: Message, state: FSMContext):
    await state.set_state(stepState.region)
    await message.answer(_('choose region'), reply_markup=region_button())
    await message.answer("Evos jamoasiga qo'shiling! \n📍 Shaharni tanlang.")
    await state.set_state(stepState.vac_)

# @vacancy_router.message(F.text == __("Back"), stepState.region)
# async def back_handler(message: Message, state: FSMContext):
#     await message.answer(text= _('Back'), reply_markup=)