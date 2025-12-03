from aiogram.types import User

from .base import BaseAPIService


class UserAPIService(BaseAPIService):
    @classmethod
    async def get_user(cls, chat_id: int) -> dict | None:
        endpoint = f'/users/{chat_id}/'
        return await cls.get(endpoint)

    @classmethod
    async def create_user(cls, user_data: User, source: str | None) -> dict | None:
        endpoint = '/users/'

        payload = {
            'chat_id': user_data.id,
            'username': user_data.username,
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
            'language': user_data.language_code,
            'source': source,
        }

        return await cls.post(endpoint, json=payload)

    @classmethod
    async def set_blocked_status(cls, chat_id: int, is_blocked: bool) -> dict | None:
        endpoint = f"/users/{chat_id}/"
        payload = {'is_active': not is_blocked}
        return await cls.patch(endpoint, json=payload)
