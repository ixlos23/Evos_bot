from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

from db.models import Region


def region_button():
    regions: list[Region] = Region().select()
    rkb = ReplyKeyboardBuilder()
    keyboards = [KeyboardButton(text=region.name)for region in regions]
    keyboards += [KeyboardButton(text=_('Back'))]
    rkb.add(*keyboards)
    rkb.adjust(2, repeat=True)
    return rkb.as_markup(resize_keyboard=True)


async def location_button():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[KeyboardButton(text="Location", request_location=True)])
    rkm = rkm.as_markup(resize_keyboard=True)
    return rkm




# company = "Kompaniya haqida🏢"
# filal = "Filali⛓"
# vac = "Bo'sh ish o'rni💼"
# menu = "Menu📱"
# news = "Yangiliklar🗣"
# admin = "Murojaat uchun📞"
# til = "🇸🇱/🇷🇺 Til"
# back= "⬅️Back"
# async def main_menu():
#     rmk = ReplyKeyboardBuilder()
#     design = [
#         KeyboardButton(text=company),
#         KeyboardButton(text=filal),
#         KeyboardButton(text=vac),
#         KeyboardButton(text=menu),
#         KeyboardButton(text=news),
#         KeyboardButton(text=admin),
#         KeyboardButton(text=til),
#
#     ]
#     rmk.add(*design)
#     rmk.adjust(2, 1, 2, 2)
#     return rmk.as_markup(resize_keyboard=True)

tosh = "Toshkent"
sam = "Samarqand"
xora = "Xorazm"
sir = "Sirdaryo"
bux = "Buxoro"
sur = "Surxondaryo"

async def filial_button():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=tosh),
        KeyboardButton(text=sam),
        KeyboardButton(text=xora),
        KeyboardButton(text=sir),
        KeyboardButton(text=bux),
        KeyboardButton(text=sur),
        KeyboardButton(text=back),
    ]
    rmk.add(*design)
    rmk.adjust(2, repeat=True)
    return rmk.as_markup(resize_keyboard=True)

near_filal = "☕️Yaqin filiallarni ko'rsatish"
center = "Bosh ofis🏢"
tosh_sh = "Toshkent Sh"
back = "⬅️Ortga"


async def tosh_button():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=near_filal),
        KeyboardButton(text=center),
        KeyboardButton(text=tosh_sh),
        KeyboardButton(text=back),
    ]
    rmk.add(*design)
    rmk.adjust(1,2,1)
    return rmk.as_markup(resize_keyboard=True)

async def pagination_btn(product_index):
    design = [
        [
            InlineKeyboardButton(text='prev', callback_data=f'prev_{product_index - 1}'),
            InlineKeyboardButton(text=str(product_index+1), callback_data=f'session_{product_index}'),
            InlineKeyboardButton(text="next", callback_data=f'next_{product_index+1}'),

        ]
    ]
    if product_index == 0:
        del design[0][0]
    return InlineKeyboardMarkup(inline_keyboard=design)


sam_dar = "📍 Samarqand Darvoza"
oloy = "📍 Oloy bozori"
queen_dis = "📍 Malika"
yahyo = "📍 Yahyo G'ulomov, 94"
back = "⬅️Ortga"


async def district_btn():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=sam_dar),
        KeyboardButton(text=oloy),
        KeyboardButton(text=queen_dis),
        KeyboardButton(text=yahyo),
        KeyboardButton(text=back),
    ]
    rmk.add(*design)
    rmk.adjust(2, 2, 1)
    return rmk.as_markup(resize_keyboard=True)

Toshkent = "Toshkent"
Qarshi = "Qarshi"
Namangan = "Namangan"
Nukus= "Nukus"
Andijon = "Andijon"
Qoqon = "Qo'qon"
Toshkent_vil = "Toshkent vil"
Samarqand = "Samarqand"
Xorazm = "Xorazm"
back = "⬅️Ortga"
log_out = "❌ Bekor qilish ❌"

async def vac_reg():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=Toshkent),
        KeyboardButton(text=Qarshi),
        KeyboardButton(text=Namangan),
        KeyboardButton(text=Andijon),
        KeyboardButton(text=Qoqon),
        KeyboardButton(text=Samarqand),
        KeyboardButton(text=Nukus),
        KeyboardButton(text=Toshkent_vil),
        KeyboardButton(text=Xorazm),
        KeyboardButton(text=back),
        KeyboardButton(text=log_out),
    ]
    rmk.add(*design)
    rmk.adjust(2, 2, 2, 2, 1, 2)
    return rmk.as_markup(resize_keyboard=True)

univer = "Universal xodim"
call_center = "Call-markaz operator"
curyer = "Kuryer"
Back = "⬅️Ortga"
log__out = "❌ Bekor qilish ❌"


async def tosh_work():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=univer),
        KeyboardButton(text=call_center),
        KeyboardButton(text=curyer),
        KeyboardButton(text=Back),
        KeyboardButton(text=log__out),
    ]
    rmk.add(*design)
    rmk.adjust(2, 1, 2)
    return rmk.as_markup(resize_keyboard=True)


Yunusobod = "Yunusobod"
Yashnobod = "Yashnobod"
Uchtepa = "Uchtepa"
Chilonzor = "Chilonzor"
Shayxontohur = "Shayxontohur"
Mirzo_Ulugbek = "Mirzo Ulug'bek"
Yakkasaroy = "Yakkasaroy"
Sergeli = "Sergeli"
Mirobod = "Yunusobod"
Olmazor = "Olmazor"
Bektemir = "Bektemir"
Backk = "⬅️Ortga"
log___out = "❌ Bekor qilish ❌"


async def univer_work_district():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=Yunusobod),
        KeyboardButton(text=Yashnobod),
        KeyboardButton(text=Uchtepa),
        KeyboardButton(text=Chilonzor),
        KeyboardButton(text=Shayxontohur),
        KeyboardButton(text=Mirzo_Ulugbek),
        KeyboardButton(text=Yakkasaroy),
        KeyboardButton(text=Sergeli),
        KeyboardButton(text=Mirobod),
        KeyboardButton(text=Olmazor),
        KeyboardButton(text=Bektemir),
        KeyboardButton(text=Backk),
        KeyboardButton(text=log___out),
    ]
    rmk.add(*design)
    rmk.adjust(2, 2, 2, 2, 2, 1, 2)
    return rmk.as_markup(resize_keyboard=True)


def lang_btn():
    rmk = ReplyKeyboardBuilder()

    design = [
        KeyboardButton(text=_("🏢 About company")),
        KeyboardButton(text=_("⛓ Branches")),
        KeyboardButton(text=_("💼  Vacancies")),
        KeyboardButton(text=_("Menu")),
        KeyboardButton(text=_("🗣 News")),
        KeyboardButton(text=_("📞 Contact/Address")),
        KeyboardButton(text=_("🇺🇿/🇺🇸 lang")),
    ]
    rmk.add(*design)
    rmk.adjust(2, 1, 2, 2)
    return rmk.as_markup(resize_keyboard=True, one_time_keyboard=True)


def lang_button():
    design = [
        [
            KeyboardButton(text=_("🇺🇿 Uzb")),
            KeyboardButton(text=_("🇺🇸 Eng")),
        ]
    ]

    rmk = ReplyKeyboardMarkup(keyboard=design, one_time_keyboard=True, resize_keyboard=True)
    return rmk
