import messages
import vk_info
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import asyncio
import json

async def gb(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н гб" in command:
        msg_1 = "🖐&#4448;  &#4448;    &#4448; &#4448; &#4448;🍺 Го бухать"
        msg_2 = "🖐&#4448;  &#4448;    &#4448; &#4448;🍺 Го бухать"
        msg_3 = "🖐&#4448;  &#4448;    &#4448;  🍺 Го бухать"
        msg_4 = "🖐&#4448;  &#4448;🍺Го бухать"
        msg_5 = "🖐 &#4448; 🍺 Го бухать"
        msg_6 = "🖐🍺Го бухать"
        msg_7 = "🖐🍺Го бухать"

        messages.write_msg(peer_id, msg_1)
        msg_id = vk_info.info_msg_id(peer_id)
        time.sleep(1)
        messages.edit_msg(peer_id, msg_2, msg_id)
        time.sleep(1)
        messages.edit_msg(peer_id, msg_3, msg_id)
        time.sleep(1)
        messages.edit_msg(peer_id, msg_4, msg_id)
        time.sleep(1)
        messages.edit_msg(peer_id, msg_5, msg_id)
        time.sleep(1)
        messages.edit_msg(peer_id, msg_6, msg_id)
        time.sleep(1)
        messages.edit_msg(peer_id, msg_7, msg_id)

with open("database_token.json", "r", encoding="utf-8") as file:
   data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait = 0)
