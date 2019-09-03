from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import TelegramClient,sync,events
from Config import *
NAME = '636788602'
client = TelegramClient(NAME, TELEGRAM_APP_API_ID, TELEGRAM_APP_API_HASH)
client.connect()
updates = client(ImportChatInviteRequest('Fsv60UdcuXxWagSGdCgouw'))
print(updates)
client.run_until_disconnected()