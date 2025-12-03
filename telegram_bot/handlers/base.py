from aiogram import Router
from aiogram.filters import KICKED, MEMBER, ChatMemberUpdatedFilter, CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import ChatMemberUpdated, Message

from telegram_bot.api import UserAPIService

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext, command: CommandObject) -> None:
    """Обработчик команды /start."""
    await state.clear()
    await UserAPIService.create_user(user_data=message.from_user, source=command.args)
    await message.answer('Добро пожаловать!')


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated) -> None:
    """Деактивирует пользователя, если он заблокировал бота."""
    await UserAPIService.set_blocked_status(chat_id=event.from_user.id, is_blocked=True)


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def user_unblocked_bot(event: ChatMemberUpdated) -> None:
    """Активирует пользователя, если он разблокировал бота."""
    await UserAPIService.set_blocked_status(chat_id=event.from_user.id, is_blocked=False)

