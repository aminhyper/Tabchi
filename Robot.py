from telethon import TelegramClient, events,sync
from Config import *
from telethon.tl.types import *
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
NAME = 'tabchi'
client = TelegramClient(NAME, TELEGRAM_APP_API_ID, TELEGRAM_APP_API_HASH)
client.start()
