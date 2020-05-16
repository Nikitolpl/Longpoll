import asyncio
import json
import time

import vk_api
from vk_api.longpoll import VkLongPoll

from tools.messages import messages

finished = True


async def online_on(delay, command):
    await asyncio.sleep(delay)
    global finished
    if "!н +онлайн" in command:
        finished = False


async def online(delay, peer_id, command):
    await asyncio.sleep(delay)
    global finished
    if "!н +онлайн" in command:
        messages.write_msg(peer_id, "✅ Вечный онлайн включён")
        while not finished:
            print("Авто онлайн работает: " + str(vk.method('account.setOnline', {'voip': 0})))
            time.sleep(180)


async def offline(delay, peer_id, command):
    await asyncio.sleep(delay)
    global finished
    if "!н -онлайн" in command:
        finished = True
        messages.write_msg(peer_id, "✅ Вечный онлайн отключён")


def online_info():
    global finished
    return finished


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
