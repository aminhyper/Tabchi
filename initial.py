from telethon import TelegramClient,sync
from Config import *

# Remember to use your own values from my.telegram.org!
api_id = TELEGRAM_APP_API_ID
api_hash = TELEGRAM_APP_API_HASH
client = TelegramClient('data', api_id, api_hash)
client.start(phone=TELEGRAM_PHONE_NUMBER)

