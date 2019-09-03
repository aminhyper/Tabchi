from telethon.sync import TelegramClient
from telethon import functions, types
from Config import *
api_id = TELEGRAM_APP_API_ID
api_hash = TELEGRAM_APP_API_HASH
name = '636788602'
with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.messages.GetMessagesViewsRequest(
        peer='hyper_design_bot',
        id=[86],
        increment=True
    ))
    for x in result:
        print(x)