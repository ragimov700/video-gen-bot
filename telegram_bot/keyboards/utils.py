from typing import Sequence

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

InlineButtons = Sequence[tuple[str, str]]


def _build_keyboard(buttons: InlineButtons, row_width: int = 2) -> InlineKeyboardMarkup:
    """Конструктор inline клавиатур."""
    rows = []
    for index in range(0, len(buttons), row_width):
        chunk = buttons[index: index + row_width]
        row = [InlineKeyboardButton(text=label, callback_data=key) for key, label in chunk]
        rows.append(row)
    return InlineKeyboardMarkup(inline_keyboard=rows)
