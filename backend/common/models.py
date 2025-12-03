from django.db import models

blank_and_null = {'blank': True, 'null': True}


class TimestampedModel(models.Model):
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        abstract = True
