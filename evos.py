import asyncio
import json
import logging
import sys
from os import getenv

import qrcode
import segno
from aiogram import Bot, Dispatcher, html, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage import redis
from aiogram.types import Message, FSInputFile, KeyboardButton, ReplyKeyboardRemove, BotCommand, CallbackQuery, \
    callback_query, InputMediaPhoto
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from button_name import \
    filial_button, back, tosh, sam, xora, sir, bux, sur, tosh_button, center, near_filal, pagination_btn, tosh_sh, \
    district_btn, sam_dar, oloy, queen_dis, yahyo, back, vac_reg, Toshkent, tosh_work, univer, univer_work_district, \
    lang_btn, lang_button, call_center, curyer, location_button
from aiogram.utils.i18n import lazy_gettext as __, I18n, FSMI18nMiddleware
from aiogram.utils.i18n import gettext as _
from dotenv import load_dotenv

from db.models import User

load_dotenv()
i18n = I18n(path="locales")

# TOKEN = ("6548196795:AAEouiORgvCYi02qb3yzImaCzjzCkhizyEE")

TOKEN = getenv("BOT_TOKEN")
main_router = Router()

register_text = "Register®️"
login_text = "Login✅"


class RegisterState(StatesGroup):
    fullname = State()
    phone_number = State()
    username = State()
    password = State()
    location = State()


class stepState(StatesGroup):
    city_button = State()
    back_btn = State()
    head_ofice = State()
    district = State()
    vac_ = State()
    univer = State()
    lang = State()
    region = State()
    new = State()


class LoginState(StatesGroup):
    username = State()
    password = State()

@main_router.message(F.text == __("Back"), stepState.region)
@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    # rkm = ReplyKeyboardBuilder()
    # rkm.add(*[KeyboardButton(text=login_text), KeyboardButton(text=register_text)])
    # rkm.adjust(2)
    # rkm = rkm.as_markup(resize_keyboard=True)
    await state.clear()
    user = {
        "user_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
    }
    user = User(**user)
    if not user.select(user_id=message.from_user.id):
        user.insert()
    await message.answer(_("Hello, {name}!").format(name=html.quote(message.from_user.full_name)),
                         reply_markup=lang_btn())  # , reply_markup=rkm)


@main_router.message(F.text == "⬅️Ortga")
async def ortga_hndlr(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Back", reply_markup=lang_btn())


@main_router.message((F.text == __("🇺🇿/🇺🇸 lang")) | (F.text == "🇺🇿/🇺🇸 til"))
async def language_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(stepState.lang)
    await message.answer(_("Language menu"), reply_markup=lang_button())


@main_router.message(stepState.lang)
async def language_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    if message.text == __("🇺🇿 Uzb"):
        await state.update_data({"locale": 'uz'})
        i18n.current_locale = 'uz'
    elif message.text == __("🇺🇸 Eng"):
        await state.update_data({"locale": 'en'})
        i18n.current_locale = 'en'

    await message.answer(_("Back"), reply_markup=lang_btn())

    path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/img.png" # noqa
    image = FSInputFile(path)
    await message.answer_photo(image)
    await message.answer("EVOS oilasiga xush kelibsiz!") # noqa
    await message.answer("Menulardan birini tanlang!") #reply_markup=await main_menu()) # noqa
    # await message.bot.set_my_commands(commands=[BotCommand(command='/start', description='Qayta ishga tushirish!')])


#     await message.answer("Buttonlardan birini tanlang👇") # noqa
#
# @main_router.message(F.text == register_text)
# async def register_handler(message: Message, state: FSMContext) -> None:
#     await state.set_state(RegisterState.fullname)
#     await message.answer("Fullname: ", reply_markup=ReplyKeyboardRemove())
#
#
# async def phone_button():
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(*[KeyboardButton(text="contact share", request_contact=True)])
#     rkm = rkm.as_markup(resize_keyboard=True)
#     return rkm
#

#
# @main_router.message(RegisterState.fullname)
# async def fullname_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data({"fullname" : message.text})
#     await state.set_state(RegisterState.phone_number)
#     rkm = await phone_button()
#     await message.answer("Telefon raqam yuborish uchun past tugmani bosing! ", reply_markup=rkm) # noqa
#
# @main_router.message(RegisterState.phone_number , F.contact)
# async def phone_number_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data({"phone_number" : message.contact.phone_number})
#     await state.set_state(RegisterState.location)
#     rkm = await location_button()
#     await message.answer("location yuborish u-n pastdagi tugmain bosing!", reply_markup=rkm) # noqa
#
# @main_router.message(RegisterState.location, F.location)
# async def location_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data({"longitude" : message.location.longitude, "latitude" :message.location.latitude})
#     await state.set_state(RegisterState.username)
#     await message.answer("username kiriting: ", reply_markup=ReplyKeyboardRemove()) # noqa
#
# @main_router.message(RegisterState.username , F.text)
# async def username_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data({"username" : message.text})
#     await state.set_state(RegisterState.password)
#     await message.answer("password kiriting: ")


# @main_router.message(RegisterState.password , F.text)
# async def password_handler(message: Message, state: FSMContext) -> None:
# password = message.text
# data = await state.get_data()
# await state.clear()
# await message.answer(f"Ma'lumotlariz:\n {str(data)} \n password: {password}")
# path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/img.png"
# image = FSInputFile(path)
# await message.answer_photo(image)
# await message.answer("EVOS oilasiga xush kelibsiz!")
# await message.answer("Menulardan birini tanlang!", reply_markup= await main_menu())


@main_router.message((F.text == "Menu") | (F.text == "Menyu"))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    with open('products.json', 'r') as f:
        products: list[dict] = json.load(f)
    await state.update_data({'products': products})
    first_product = products[0]
    product_index = 0
    caption = f"""
Title: {first_product.get('title')}
Price: {first_product.get('price')}
    """
    await message.answer_photo(photo=first_product.get('images')[0], caption=caption,
                               reply_markup=await pagination_btn(product_index))


@main_router.callback_query(F.data.startswith('next_') | (F.data.startswith('prev_')) | (F.data.startswith('back_')))
async def next_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    product_index = int(callback_query.data.split('_')[1])
    data = await state.get_data()
    products = data.get('products')
    session_product = products[product_index]
    caption = f"""
Title: {session_product.get('title')}
Price: {session_product.get('price')}
        """
    await callback_query.message.edit_media(media=InputMediaPhoto(media=session_product.get('images')[0]), caption=caption,
                                              reply_markup=await pagination_btn(product_index))


@main_router.message((F.text == "🏢 About company") | (F.text == "🏢 Kampaniya haqida") )
async def company_handler(message: Message) -> None:
    path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/photo_2024-05-22_15-16-11.jpg"
    image = FSInputFile(path)
    await message.answer_photo(image)
    await message.answer("""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi
va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va
EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir.        EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


@main_router.message((F.text == "⛓ Branches") | (F.text == "⛓ Filial"))
async def filial_button1(message: Message, state: FSMContext) -> None:
    rmk = await filial_button()
    await message.answer("Shahar tanlang👇", reply_markup=rmk)
    await state.set_state(stepState.city_button)


@main_router.message(stepState.city_button)
async def main_button_handler(message: Message, state: FSMContext) -> None:
    if message.text == tosh:
        await message.answer(tosh)
        path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/photo_2024-05-25_11-15-06.jpg"
        image = FSInputFile(path)
        await message.answer_photo(image)
        await message.answer("""EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi.
Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.
Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila.
EVOS har kuni kengayib bormoqda,
bugungi kunda bizda bir yarim mingdan ortiq odam bor.
Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!""", reply_markup=await tosh_button())
        await state.set_state(stepState.head_ofice)


    # elif message.text == sam:
    #     await message.answer(sam)
    # elif message.text == xora:
    #     await message.answer(xora)
    # elif message.text == sir:
    #     await message.answer(sir)
    # elif message.text == bux:
    #     await message.answer(bux)
    # elif message.text == sur:
    #     await message.answer(sur)
    # elif message.text == back:
    #     pass

@main_router.message(stepState.head_ofice, F.text)
async def main_button_handler(message: Message, state: FSMContext) -> None:
    if message.text == near_filal:
        await state.update_data({"longitude" : message.location.longitude, "latitude" :message.location.latitude})
        await message.answer("location yuborish u-n pastdagi tugmain bosing!", reply_markup = await location_button())

    if message.text == center:
        path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/evvoossphoto_2024-05-26_12-10-54.jpg"
        image = FSInputFile(path)
        await message.answer_photo(image)
        await message.answer("""Manzil:  Furqat ko'chasi 175, 1-kirish, 4-qavat.
    1Mo'ljal: MAKRO THE TOWER
    
    Kontakt: +998712031212""")
        await message.answer_location(latitude=41.302196, longitude=69.248867)
    if message.text == tosh_sh:
        await message.answer("Toshkent Sh", reply_markup= await district_btn())
        await state.set_state(stepState.new)


@main_router.message(stepState.new, F.text)
async def district_handler(message: Message, state: FSMContext) -> None:
        if message.text == sam_dar:
            path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/sam_dar_2024-05-26_12-05-46.jpg"
            image = FSInputFile(path)
            await message.answer_photo(image)
            await message.answer("""
    Filial: "Samarqand Darvoza"

    Manzil: Qoratosh, 5A""")
            await message.answer_location(latitude=41.316428, longitude=69.230965)
        if message.text == oloy:
            path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/oloy_4-05-28_15-40-33.jpg"
            image = FSInputFile(path)
            await message.answer_photo(image)
            await message.answer("""
    Filial: Oloy bozori

    Manzil: Amir Temur prospekti, 42

    Kontakt: +998 71 203 12 12""")
            await message.answer_location(latitude=41.32, longitude= 69.282572)
        if message.text == queen_dis:
            await message.answer(queen_dis)
        if message.text == yahyo:
            await message.answer(yahyo)






# @main_router.message(F.text == near_filal)
# async def near_filal_handler(message: Message, state: FSMContext) -> None:
#     rkm = await location_button()
#     await state.update_data({"longitude" : message.location.longitude, "latitude" :message.location.latitude})
#     await message.answer("location yuborish u-n pastdagi tugmain bosing!", reply_markup=rkm)
#
#
# @main_router.message(F.text == center, stepState.head_ofice)
# async def center_button(message: Message, state: FSMContext) -> None:
#     path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/evvoossphoto_2024-05-26_12-10-54.jpg"
#     image = FSInputFile(path)
#     await message.answer_photo(image)
#     await message.answer("""Manzil:  Furqat ko'chasi 175, 1-kirish, 4-qavat.
# 1Mo'ljal: MAKRO THE TOWER
#
# Kontakt: +998712031212""")
#     await message.answer_location(latitude=41.302196, longitude=69.248867)
#
#
# @main_router.message(F.text == tosh_sh)
# async def district_handler(message: Message, state: FSMContext) -> None:
#     if message.text == sam_dar:
#         path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/sam_dar_2024-05-26_12-05-46.jpg"
#         image = FSInputFile(path)
#         await message.answer_photo(image)
#         await message.answer("""
# Filial: "Samarqand Darvoza"
#
# Manzil: Qoratosh, 5A""")
#         await message.answer_location(latitude=41.316428, longitude=69.230965)
#     if message.text == oloy:
#         path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/oloy_4-05-28_15-40-33.jpg"
#         image = FSInputFile(path)
#         await message.answer_photo(image)
#         await message.answer("""
# Filial: Oloy bozori
#
# Manzil: Amir Temur prospekti, 42
#
# Kontakt: +998 71 203 12 12""")
#         await message.answer_location(latitude=41.32, longitude= 69.282572)
#     if message.text == queen_dis:
#         await message.answer(queen_dis)
#     if message.text == yahyo:
#         await message.answer(yahyo)


@main_router.message((F.text == "🗣 News" ) | (F.text == "🗣 Yangiliklar"))
async def news_handler(message: Message, state: FSMContext) -> None:
    await message.answer("""
Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")


@main_router.message((F.text == "📞 Contact/Address") | (F.text =="📞 Admin/Manzil"))
async def admin_button(message: Message, state: FSMContext) -> None:
    path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/evos_murojat_2024-05-28_15-49-39.jpg"
    image = FSInputFile(path)
    await message.answer_photo(image)
    await message.answer("""
Manzil: Furqat ko'chasi 175, kirish 1,
2-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998 71 203 12 12""")
    await message.answer_location(latitude=41.302196, longitude=69.248867)


@main_router.message((F.text == "💼  Vacancies") | (F.text == "💼  Bo'sh ish o'rin"))
async def vac_button(message: Message, state: FSMContext) -> None:
    await message.answer("Evos jamoasiga qo'shiling! \n📍 Shaharni tanlang.", reply_markup= await vac_reg())
    await state.set_state(stepState.vac_)


@main_router.message(stepState.vac_, F.text)
async def vac_button(message: Message, state: FSMContext) -> None:
    if message.text == Toshkent:
        await message.answer("💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=await tosh_work())
        await state.set_state(stepState.univer)


@main_router.message(stepState.univer, F.text)
async def work_type(message: Message, state: FSMContext) -> None:
    if message.text == univer:
        path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/univer_2024-05-28_16-38-02.jpg"
        image = FSInputFile(path)
        await message.answer_photo(image)
        await message.answer("""
🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 Erkin jadval (iloji bo'lsa)

✔️ Yoqimli tashqi ko'rinish

💰 Ish haqi 17228.96 dan (soliqlargacha) bir soatiga""")

    if message.text == call_center:
        path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/call.png"
        image = FSInputFile(path)
        await message.answer_photo(image)
        await message.answer("""
📌 Yosh 18 dan 35 gacha

🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 To'liq bandlik

👨‍💼/👩‍💼 Chiroyli ko'rinish

🧑‍💻/👩‍💻 Kompyuter yoki noutbuk bo'lishi kerak
Biz taqdim etamiz:
- Rasmiy ish
- Kompaniya tomonidan taqdim etiladigan ovqatlanish
- Birinchi ish kuningizdan hisoblanadigan  ish xaqi
- Soatlik ish haqi""")

    if message.text == curyer:
        path = "/home/ixlos/PycharmProjects/p23/P23/module_5/lesson_2/home_task_evos/kuryer_2024-06-10_00-42-42.jpg"
        image = FSInputFile(path)
        await message.answer_photo(image)
        await message.answer("""
📌 Yosh 20 dan 35 gacha

🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 Erkin jadval (iloji bo'lsa)

👨‍💼/👩‍💼 Chiroyli ko'rinish

🚘 Shaxsiy transport bo'lishligi shart

📍Oylik maosh joylashuv va regonga qarab""")


# @main_router.message(F.text == "⬅Ortga")
# async def ortga_hndlr(message: Message, state: FSMContext) -> None:
#     await state.clear()
#     await message.answer("Back", reply_markup=await tosh_work())


# ==================================== Login==================================
# @main_router.message(F.text == login_text)
# async def register_handler(message: Message, state: FSMContext) -> None:
#     await state.set_state(LoginState.username)
#     await message.answer("username: ", reply_markup=ReplyKeyboardRemove())
#
#
# @main_router.message(LoginState.username, F.text)
# async def username_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data({"username": message.text})
#     await state.set_state(LoginState.password)
#     await message.answer("password: ", reply_markup=ReplyKeyboardRemove())
#
#
# @main_router.message(LoginState.password, F.text)
# async def username_handler(message: Message, state: FSMContext) -> None:
#     password = message.text
#     data = await state.get_data()
#     user = member().select(username=data.get('username'), password=password)
#     if user:
#         await message.answer('Success!', reply_markup=ReplyKeyboardRemove())
#     else:
#         await message.answer('Not found account!', reply_markup=ReplyKeyboardRemove())
#     await state.clear()
#     await message.answer("Finish! ", reply_markup=ReplyKeyboardRemove())



