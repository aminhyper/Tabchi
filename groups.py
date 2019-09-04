from telethon import TelegramClient,sync
from telethon.tl.types import InputUser
from Config import *
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.functions.messages import AddChatUserRequest
api_id = TELEGRAM_APP_API_ID
api_hash = TELEGRAM_APP_API_HASH
client = TelegramClient(session_name, api_id, api_hash)
client.connect()
def get_input_user(uid):
    """
    create telegram user instance
    """
    return InputUser(uid, 0)
def create_group(uids, group_name):
    """
    create telegram group for given users list
    """
    users = list(map(get_input_user, uids))
    group = CreateChatRequest(users, group_name)
    try:
        result = client.invoke(group)
        return result, False
    except Exception as e:
        return e, True
def add_member_to_group(uid, group_id, fwd_limit=10):
    """
    add member to existing group
    """
    user = get_input_user(uid)
    user_request = AddChatUserRequest(group_id, user, fwd_limit)
    try:
        result = client.invoke(user_request)
        return result, False
    except Exception as e:
        return e, True
print(get_input_user('72608783'))