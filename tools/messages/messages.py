import json
import random

import vk_api
from vk_api.longpoll import VkLongPoll


def write_msg(peer_id: int, message: str):
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(0, 2048),
                                'disable_mentions': 1})


def edit_msg(peer_id, message, msg_id):
    vk.method('messages.edit', {'peer_id': peer_id, 'message': message, 'message_id': msg_id})


def edita_msg(peer_id, message, attachments, msg_id):
    vk.method('messages.edit',
              {'peer_id': peer_id, 'message': message, 'attachment': attachments, 'message_id': msg_id})


def delete_msg(msg_id: int):
    vk.method("messages.delete", {'message_ids': msg_id, 'delete_for_all': 1})


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
