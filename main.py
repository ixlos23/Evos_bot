import asyncio
import logging

import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.i18n import FSMI18nMiddleware
from telegram.constants import ParseMode

from evos import main_router, TOKEN, i18n
from vacancy import vacancy_router


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(*[main_router, vacancy_router])
    dp.update.middleware(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    """
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ixlos23/Evos_bot.git
git push -u origin main"""