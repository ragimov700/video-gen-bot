import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from loguru import logger

from .config import TELEGRAM_BOT_TOKEN
from .router import setup_routers

logger.remove()
logger.add(
    sys.stdout,
    level='DEBUG',
    format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
    backtrace=True,
    colorize=True
)

bot = Bot(
    TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True),
)
dp = Dispatcher()
setup_routers(dp)


async def main() -> None:
    """Запуск бота."""
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
