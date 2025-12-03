from django.db import models

from common.models import blank_and_null, TimestampedModel


class TelegramUser(TimestampedModel):
    """Модель для телеграм пользователей."""

    chat_id = models.BigIntegerField('Чат ид', db_index=True, unique=True)
    username = models.CharField('Юзернейм', max_length=255, **blank_and_null)
    first_name = models.CharField('Имя', max_length=255, **blank_and_null)
    last_name = models.CharField('Фамилия', max_length=255, **blank_and_null)
    is_active = models.BooleanField('Активен', default=True)
    language = models.CharField('Язык', max_length=16, **blank_and_null)
    source = models.CharField('Источник перехода', max_length=256, **blank_and_null)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'Пользователь {self.chat_id}'
