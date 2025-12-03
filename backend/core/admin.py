from django.contrib import admin

from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'username', 'first_name', 'last_name', 'is_active')
    search_fields = ('chat_id', 'username', 'first_name', 'last_name')
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fields = (
        'chat_id',
        'username',
        'first_name',
        'last_name',
        'is_active',
        'language',
        'source',
        'created_at',
        'updated_at'
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
