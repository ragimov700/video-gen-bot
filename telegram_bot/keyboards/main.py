from aiogram.types import InlineKeyboardMarkup

from .utils import InlineButtons, _build_keyboard

MAIN: InlineButtons = (
    ("video_from_text", "📝 Видео из текста"),
    ("video_one_photo", "🖼️ Видео из фото"),
    ("prompts_menu", "💡 Готовые промпты"),
    ("settings_menu", "⚙️ Настройки"),
    ("balance_menu", "💰 Баланс и оплата"),
    ("free_generation", "🎁 Бесплатная генерация"),
)


def main_keyboard() -> InlineKeyboardMarkup:
    """Кнопки главного меню."""
    return _build_keyboard(buttons=MAIN, row_width=1)
