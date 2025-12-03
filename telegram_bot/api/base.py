import logging

import aiohttp

from telegram_bot.config import BACKEND_API_URL


class BaseAPIService:
    BASE_URL = BACKEND_API_URL
    TIMEOUT = aiohttp.ClientTimeout(total=5)

    @classmethod
    async def get(cls, endpoint: str, params: dict | None = None) -> dict | None:
        url = f'{cls.BASE_URL}{endpoint}'
        try:
            async with aiohttp.ClientSession(timeout=cls.TIMEOUT) as session:
                async with session.get(url, params=params) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            logging.error(e)
            return None

    @classmethod
    async def post(
        cls,
        endpoint: str,
        data: dict | None = None,
        json: dict | None = None
    ) -> dict | None:
        url = f"{cls.BASE_URL}{endpoint}"
        try:
            async with aiohttp.ClientSession(timeout=cls.TIMEOUT) as session:
                async with session.post(
                        url,
                        data=data,
                        json=json,
                ) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            logging.error(e)
            return None

    @classmethod
    async def patch(
        cls,
        endpoint: str,
        data: dict | None = None,
        json: dict | None = None
    ) -> dict | None:
        url = f'{cls.BASE_URL}{endpoint}'
        try:
            async with aiohttp.ClientSession(timeout=cls.TIMEOUT) as session:
                async with session.patch(
                        url,
                        data=data,
                        json=json,
                ) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            logging.error(e)
            return None