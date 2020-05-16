import asyncio
import json
import re
from typing import List, Any, Optional
import random
import time
import datetime

import vk_api
from vk_api.longpoll import VkLongPoll

from tools.messages import messages

start = False
finish = True


async def dr(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н дата" in command:
        history: Optional[Any] = vk.method('messages.getHistory',
                                           {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text: object = history['items'][0]['text']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args: List[Any] = []
        payload: str = ""
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]

        if len(args) == 1:
            argss = None
            messages.write_msg(peer_id, "❗ Укажите дату, которую хотите поставить на своё день рождения")
        else:
            argss = args[1:]
            datadr = ''.join(argss)
            try:
                vk.method("account.saveProfileInfo", {'bdate': datadr})
                messages.write_msg(peer_id, "✅ Дата дня рождения успешно изменена")
            except:
                msg = "❗ Дата рождения пользователя должна в формате DD.MM.YYYY, например \"15.11.1984\""
                messages.write_msg(peer_id, msg)


async def status(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н статус" in command:
        history: Optional[Any] = vk.method('messages.getHistory',
                                           {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text: object = history['items'][0]['text']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args: List[Any] = []
        payload: str = ""
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]
        argss = args[1:]
        payload = "".join(payload)
        if payload == "":
            messages.write_msg(peer_id, "❗ Укажите текст нового статуса (со второй строки)")
            pass
        elif payload != "":
            try:
                vk.method("status.set", {'text': payload})
                messages.write_msg(peer_id, "✅ Статус успешно изменён")
            except:
                msg = "❗ Ошибка при выполнении смены статуса"
                messages.write_msg(peer_id, msg)


async def autodr_on(delay, command):
    global start
    await asyncio.sleep(delay)
    if "!н +адр" in command:
        start = True


async def autodr(delay, peer_id, command):
    global start
    await asyncio.sleep(delay)
    if "!н +адр" in command:
        history: Optional[Any] = vk.method('messages.getHistory',
                                           {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text: object = history['items'][0]['text']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args: List[Any] = []
        payload: str = ""
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]

        if len(args) == 1:
            argss = None
            messages.write_msg(peer_id, "❗ Укажите задержку перед новым обновлением вашей даты др")
        else:
            argss = args[1:]
            sleep = ''.join(argss)
            try:
                sleep = int(sleep)
            except:
                messages.write_msg(peer_id, "❗ Задержка должна быть в числовом формате.")
            datadr = [
                "01.01.1999", "03.12.2005",
                "12.03.2001", "14.05.2004",
                "07.10.2005", "10.11.2003",
                "11.06.1999", "15.13.2002",
                "31.07.2001", "23.10.2000",
                "04.04.2004", "06.06.2005",
                "05.09.2001", "14.06.2005",
                "11.11.2003", "25.04.2002",
                "13.05.2000", "15.10.2001",
                "31.10.2003", "12.02.2000"
            ]
            messages.write_msg(peer_id, "✅ Автоматическая смена дня рождения включена")

            while start:
                vk.method("account.saveProfileInfo", {'bdate': random.choice(datadr)})
                print("Автосмена др работает")
                time.sleep(sleep)


async def autodr_off(delay, peer_id, command):
    global start
    await asyncio.sleep(delay)
    if "!н -адр" in command:
        start = False
        messages.write_msg(peer_id, "✅ Автоматическая смена дня рождения выключена")


def info_autodr():
    global start
    return start


async def autostatus_on(delay, command):
    global finish
    await asyncio.sleep(delay)
    if "!н +аст" in command:
        finish = False


async def autostatus(delay, peer_id, command):
    global finish
    await asyncio.sleep(delay)
    if "!н +аст" in command:
        history: Optional[Any] = vk.method('messages.getHistory',
                                           {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text: object = history['items'][0]['text']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args: List[Any] = []
        payload: str = ""
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]

        if len(args) == 1:
            argss = None
            messages.write_msg(peer_id, "❗ Укажите ваш часовой пояс (разница от UTC (для моск. время - \"3\"))")
        else:
            argss = args[1:]
            hours = ''.join(argss)
            try:
                hours = int(hours)
            except:
                messages.write_msg(peer_id, "❗ Часовой пояс должен быть в числовом формате.")

            messages.write_msg(peer_id, "✅ Автостатус запущен")
            while not finish:  # Запускаем бесконечный цикл
                delta = datetime.timedelta(hours=hours, minutes=0)
                t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Присваиваем дату и время переменной «t»
                nowtime = t.strftime("%H:%M")  # текущее время
                nowdate = t.strftime("%d.%m.%Y")  # текущее дата
                on = vk.method("friends.getOnline")  # получаем список id друзей онлайн
                counted = len(on)  # подсчет кол-ва друзей
                vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})
                time.sleep(30)  # анти-каптча. Погружает скрипт в «сон» на 30 секун


async def autostatus_off(delay, peer_id, command):
    global finish
    await asyncio.sleep(delay)
    if "!н -аст" in command:
        finish = True
        messages.write_msg(peer_id, "✅ Автостатус выключен")


def info_autostatus():
    global finish
    return finish


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']
# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)