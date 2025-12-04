from aiogram import Router, types, F
from aiogram.filters import (
    KICKED,
    MEMBER,
    ChatMemberUpdatedFilter,
    CommandStart,
    CommandObject,
    Command,
)
from aiogram.fsm.context import FSMContext
from aiogram.types import ChatMemberUpdated, Message
from loguru import logger

from telegram_bot.api import UserAPIService
from telegram_bot.keyboards import main_keyboard
from telegram_bot.texts import START_TEXT

router = Router()


@router.message(CommandStart())
async def command_start(msg: Message, state: FSMContext, command: CommandObject) -> None:
    """Обработчик команды /start."""
    logger.info(f'/start от {msg.from_user.id} ({msg.from_user.full_name})')
    await state.clear()
    await UserAPIService.create_user(user_data=msg.from_user, source=command.args)
    await msg.answer(
        text=START_TEXT.format(full_name=msg.from_user.full_name),
        reply_markup=main_keyboard()
    )


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated) -> None:
    """Деактивирует пользователя, если он заблокировал бота."""
    logger.info(f'Пользователь {event.from_user.id} заблокировал бота')
    await UserAPIService.set_blocked_status(chat_id=event.from_user.id, is_blocked=True)


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def user_unblocked_bot(event: ChatMemberUpdated) -> None:
    """Активирует пользователя, если он разблокировал бота."""
    logger.info(f'Пользователь {event.from_user.id} разблокировал бота')
    await UserAPIService.set_blocked_status(chat_id=event.from_user.id, is_blocked=False)


@router.message(Command('donate'))
async def donate_stars(msg: types.Message) -> None:
    logger.info(f'Пользователь {msg.from_user.id} вызвал /donate: {msg.text!r}')
    amount = msg.text.split()[-1]
    if not amount.isdigit():
        await msg.answer('Введите <b>/donate {сумма}</b>')
        return
    await msg.answer_invoice(
        title='Поддержка бота через Stars',
        description='Вы поможете развитию функционала, стабильности и новым возможностям проекта.',
        payload='donate',
        currency='XTR',
        prices=[types.LabeledPrice(label='XTR', amount=int(amount))],
    )


@router.pre_checkout_query()
async def on_pre_checkout_query(query: types.PreCheckoutQuery) -> None:
    logger.debug(f'Подтверждение оплаты от {query.from_user.id}')
    await query.answer(ok=True)


@router.message(F.successful_payment)
async def on_successful_payment(msg: types.Message) -> None:
    logger.info(f'Пользователь {msg.from_user.id} успешно оплатил поддержку')
    await msg.answer('Спасибо за поддержку! 🤝\nЭто поможет развитию бота.')
