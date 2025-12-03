from aiogram import Dispatcher
from .handlers import main


def setup_routers(dp: Dispatcher):
    dp.include_router(main.router)
