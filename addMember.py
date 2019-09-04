from telethon.sync import TelegramClient
from Config import *
api_id = TELEGRAM_APP_API_ID
api_hash = TELEGRAM_APP_API_HASH
client = TelegramClient(session_name, api_id, api_hash)
