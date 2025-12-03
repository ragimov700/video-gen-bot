from os import getenv

DEBUG = getenv('DEBUG', 'false').lower() == 'true'

TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN', '')

BACKEND_API_URL = 'http://backend:8000/api' if DEBUG else 'http://nginx:8080/api'
