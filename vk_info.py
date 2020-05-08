from typing import List, Optional, Any

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from threading import Timer
from datetime import datetime
import time
import typing
import re
import json


def get_all_history_gens(peer_id: int) -> typing.Generator[dict, None, None]:
    offset = 0
    chat = vk.method("messages.getHistory", {'count': 1, 'peer_id': peer_id, 'offset': offset})
    count = chat['count']
    while offset < count:
        try:
            chat = vk.method(
                "messages.getHistory",
                dict(count=200, peer_id=peer_id, offset=offset))
        except:
            time.sleep(3)
            continue

        offset += 200
        for item in chat['items']:
            yield item


def get_all_history_gen_dd(peer_id: int) -> typing.Generator[dict, None, None]:
    offset = 0
    chat = vk.method("messages.getHistory", {'count': 1, 'peer_id': peer_id, 'offset': offset})
    count = chat['count']
    while offset < count:
        try:
            chat = vk.method(
                "messages.getHistory",
                dict(count=20, peer_id=peer_id, offset=offset))
        except:
            time.sleep(3)
            continue

        offset += 200
        for item in chat['items']:
            yield item


def get_all_history_gens_dd(peer_id: int, counts: int) -> List[str]:
    offset = 0
    chat = vk.method("messages.getHistory",
                     dict(count=1, peer_id=peer_id, offset=offset))
    count: int = chat['count']
    user_id: list = vk.method('users.get', {})
    user_id = user_id[0]['id']
    while offset < count:
        try:
            chat = vk.method(
                "messages.getHistory",
                dict(count=200, peer_id=peer_id, offset=offset))
        except:
            time.sleep(3)
            continue

    msg_idss = []
    for i in range(len(chat)):
        if chat['items'][0]['from_id'] == user_id:
            msg_idss.append(str(chat['items'][0]['id']))

    msg_ids = []
    for i in range(counts):
        msg_ids.append(msg_idss[i])

    return msg_ids


def get_all_history_gen(peer_id: int, counts: int) -> typing.Generator[dict, None, None]:
    offset = 0
    chat = vk.method("messages.getHistory", {'count': 1, 'peer_id': peer_id, 'offset': offset})
    count = chat['count']
    while offset < count:
        try:
            chat = vk.method(
                "messages.getHistory",
                {'count': counts,
                 'peer_id': peer_id,
                 'offset': offset
                 })
        except:
            time.sleep(3)
            continue

        offset += 200
        for item in chat['items']:
            yield item


def all_members(peer_id: int) -> typing.Generator[dict, None, None]:
    chat = vk.method(
        "messages.getConversationMembers",
        {'peer_id': peer_id,
         })
    for item in chat['items']:
        yield item


def start(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
    return history


def info_msg_from_id(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
    msg_id = history['items'][0]['from_id']
    return msg_id


def info_msg_id(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
    msg_id = history['items'][0]['id']
    # nonlocal msg_id
    return msg_id


def info_msg_text(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
    msg_text = history['items'][0]['text']
    return msg_text


def info_msg_date(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
    msg_date = history['items'][0]['date']
    c_time = datetime.now().timestamp()
    delta = round(c_time - msg_date, 2)
    return delta


def info_for_me(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
    msg_id = history['items'][0]['from_id']
    msg_text = history['items'][0]['text']
    user_id = vk.method('users.get', {})
    user_id = user_id[0]['id']

    if msg_id == user_id:
        return msg_text
    else:
        print("Отправленно не от Вас")


def command(text):
    command = text
    return command


with open("database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
