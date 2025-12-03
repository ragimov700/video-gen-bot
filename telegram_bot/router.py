from aiogram import Dispatcher
from .handlers import base


def setup_routers(dp: Dispatcher):
    dp.include_router(base.router)
