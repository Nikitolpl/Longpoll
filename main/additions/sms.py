import asyncio
import json
import re
import time
from datetime import datetime
from threading import Timer
from typing import List, Any, Optional

import vk_api
from vk_api.longpoll import VkLongPoll

from tools.messages import messages
from tools.requests import vk_info


def delete_msg(msg_id: int):
    vk.method("messages.delete", {'message_ids': msg_id, 'delete_for_all': 1})


async def add_sms(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н +смс" in command:
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
        else:
            argss = args[1:]

        count = ''.join(argss)
        count = int(count)
        msg_1 = ''.join(payload)

        messages.write_msg(peer_id, "...Отправляю сообщения...")
        i = 1
        while i <= count:
            messages.write_msg(peer_id, msg_1)
            time.sleep(1)
            i = i + 1
        messages.write_msg(peer_id, "✅ Сообщения отправленны!")


async def add_spam(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н спам" in command:
        history = vk.method('messages.getHistory',
                            {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text: object = history['items'][0]['text']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args: List[Any] = []
        payload: str = ""
        arg: list
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]
        if len(args) == 1:
            argss: list = []
        else:
            argss: list = args[1:]

        count = ''.join(argss)
        count = float(count)
        msg_1 = ''.join(payload)

        messages.write_msg(peer_id, "...Отправляю сообщения...")
        i = 1
        while i >= 0:
            messages.write_msg(peer_id, msg_1)
            time.sleep(count)

        messages.write_msg(peer_id, "✅ Сообщения отправленны!")


async def add_vsms(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н влс" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text = history['items'][0]['text']
        to = history['items'][0]['reply_message']['from_id']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: list = re.findall(regexp, msg_text)
        args = []
        payload = ""
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]

        msg_1 = ''.join(payload)

        messages.write_msg(to, msg_1)

        messages.write_msg(peer_id, "✅ Сообщение отправленно в лс!")


async def del_sms(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н -с" in command:
        history: Optional[Any] = vk.method('messages.getHistory',
                                           dict(count=1, peer_id=peer_id, rev=0))
        msg_text: object = history['items'][0]['text']
        peer_id = peer_id
        user_id: Optional[Any] = vk.method('users.get', {})
        user_id = user_id[0]['id']
        print(user_id)
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args = []
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])

        if len(args) == 1:
            messages.write_msg(peer_id, "... удаляю сообщения ...\nМеня не было в этом чате :)")

            msg_ids: List[str] = []
            mmsg: dict
            for mmsg in vk_info.get_all_history_gens(peer_id):
                if datetime.now().timestamp() - mmsg['date'] > 86400:
                    break
                if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
                    msg_ids.append(str(mmsg['id']))
            message_id = 0
            try:
                vk.method("messages.delete", {'message_ids': ",".join(msg_ids), 'delete_for_all': 1})
                message_id = messages.write_msg(peer_id, "✅ Сообщения удалены\nЗабудьте об этом дежурном")
            except:
                message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

            t = Timer(2, delete_msg(msg_ids), message_id)
            t.start()
        else:
            commands = args[0].lower()
            argss = args[1:]
            count = ''.join(argss)
            count = int(count)
            messages.write_msg(peer_id, "... удаляю сообщения ...\nМеня не было в этом чате :)")
            msg_ids = []
            for mmsg in vk_info.get_all_history_gen(peer_id, count):
                if datetime.now().timestamp() - mmsg['date'] > 86400:
                    break
                if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
                    msg_ids.append(str(mmsg['id']))
            message_id = 0
            try:
                vk.method("messages.delete", {'message_ids': ",".join(msg_ids), 'delete_for_all': 1})
                message_id = messages.write_msg(peer_id, "✅ Сообщения удалены\nЗабудьте об этом дежурном")
            except:
                message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

            t = Timer(2, delete_msg(msg_ids), message_id)
            t.start()


# noinspection PyTypeChecker
async def dd_sms(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н дд" in command or "!н Дд" in command:
        history: Optional[Any] = vk.method('messages.getHistory',
                                           {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_text: object = history['items'][0]['text']
        peer_id: object = peer_id
        user_id: Optional[Any] = vk.method('users.get', {})
        user_id = user_id[0]['id']
        regexp: str = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args: List[Any] = re.findall(str(regexp), str(msg_text))
        args = []
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
        if len(args) == 1:
            msg_ids: List[str] = []
            for mmsg in vk_info.get_all_history_gens(peer_id):
                if datetime.now().timestamp() - mmsg['date'] > 86400:
                    break
                if mmsg['from_id'] == user_id and None == mmsg.get('action', None):
                    msg_ids.append(str(mmsg['id']))
            try:
                vk.method("messages.delete", dict(message_ids=",".join(msg_ids), delete_for_all=1))
                message_id = messages.write_msg(peer_id, "✅ Сообщения удалены\nЗабудьте об этом дежурном")
            except:
                message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

            t = Timer(2, delete_msg(msg_ids), message_id)
            t.start()
        else:
            argss = args[1:]
            count = ''.join(argss)
            count = int(count)
            msg_ids = []
            for mmsg in vk_info.get_all_history_gen_dd(peer_id):
                if datetime.now().timestamp() - mmsg['date'] > 86400:
                    break
                if mmsg['from_id'] == user_id and None == mmsg.get('action', None):
                    msg_ids.append(str(mmsg['id']))

            msg_idss = []
            for i in range(count):
                msg_idss.append(msg_ids[i])
                messages.edit_msg(peer_id, "&#13;", msg_ids[i])
            message_id = 0
            print(msg_idss)
            try:
                vk.method("messages.delete", {'message_ids': ",".join(msg_idss), 'delete_for_all': 1})
            except:
                message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

            t = Timer(2, delete_msg(msg_idss), message_id)
            t.start()


async def del_sms_from_user(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н -фс" in command or "!банхаммер" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = history['items'][0]['conversation_message_id']
        msg_text = history['items'][0]['text']
        peer_id = peer_id
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        user_id = history['items'][0]['reply_message']['from_id']

        messages.write_msg(peer_id, "... удаляю сообщения ...\nРейда не будет!")

        msg_ids = []
        for mmsg in vk_info.get_all_history_gens(peer_id):
            if datetime.now().timestamp() - mmsg['date'] > 86400:
                break
            if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
                msg_ids.append(str(mmsg['id']))
        message_id = 0
        try:
            vk.method("messages.delete", {'message_ids': ",".join(msg_ids), 'delete_for_all': 1})
            message_id = messages.write_msg(peer_id, "✅ Сообщения удалены\nРейдеры повержены!")
        except:
            message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

        t = Timer(2, delete_msg(msg_ids), message_id)
        t.start()


async def ban_user(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н бан" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = history['items'][0]['conversation_message_id']
        msg_text = history['items'][0]['text']
        peer_id = peer_id
        chat_id = peer_id - 2000000000

        regexp = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args = re.findall(regexp, msg_text)
        args = []
        payload = ""

        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]

        if len(args) == 1:
            commands = args[0].lower()
            argss = None

            user_id = history['items'][0]['reply_message']['from_id']
            user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status'})
            name = user[0]['first_name']

            messages.write_msg(peer_id, f"Пользователь @id{user_id}({name}) заблокирован!")
            vk.method('messages.removeChatUser', {'chat_id': chat_id, 'user_id': user_id})

            messages.write_msg(peer_id, "... удаляю сообщения ...\nРейда не будет!")

            msg_ids = []
            for mmsg in vk_info.get_all_history_gens(peer_id):
                if datetime.now().timestamp() - mmsg['date'] > 86400:
                    break
                if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
                    msg_ids.append(str(mmsg['id']))
            message_id = 0
            try:
                vk.method("messages.delete", {'message_ids': ",".join(msg_ids), 'delete_for_all': 1})
                message_id = messages.write_msg(peer_id, "✅ Сообщения удалены\nРейдеры повержены!")
            except:
                message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

            t = Timer(2, delete_msg(msg_ids), message_id)
            t.start()
        else:
            commands = args[0].lower()
            argss = args[1:]
            users_id = ''.join(argss).replace('https://vk.com/', '')
            user = vk.method('users.get', {'user_ids': users_id, 'fields': 'friend_status'})
            name = user[0]['first_name']
            user_id = user[0]['id']
            user_id = int(user_id)

            messages.write_msg(peer_id, f"Пользователь @id{user_id}({name}) заблокирован!")
            vk.method('messages.removeChatUser', {'chat_id': chat_id, 'user_id': user_id})

            messages.write_msg(peer_id, "... удаляю сообщения ...\nРейда не будет!")

            msg_ids = []
            for mmsg in vk_info.get_all_history_gens(peer_id):
                if datetime.now().timestamp() - mmsg['date'] > 86400:
                    break
                if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
                    msg_ids.append(str(mmsg['id']))
            message_id = 0
            try:
                vk.method("messages.delete", {'message_ids': ",".join(msg_ids), 'delete_for_all': 1})
                message_id = messages.write_msg(peer_id, "✅ Сообщения удалены\nРейдеры повержены!")
            except:
                message_id = messages.write_msg(peer_id, f"❗ Не удалось удалить сообщения.")

            t = Timer(2, delete_msg(msg_ids), message_id)
            t.start()


async def add_user(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н добавить" in command or "!н вернуть" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = history['items'][0]['conversation_message_id']
        msg_text = history['items'][0]['text']
        peer_id = peer_id
        chat_id = peer_id - 2000000000

        regexp = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        _args = re.findall(regexp, msg_text)
        args = []
        payload = ""
        for arg in _args:
            if arg[1] != '':
                args.append(arg[1])
            if arg[2] != '':
                payload = arg[2][1:]

        if len(args) == 1:
            commands = args[0].lower()
            argss = None
            messages.write_msg(peer_id, "Ссылка на пользователя не указана!")
        else:
            commands = args[0].lower()
            argss = args[1:]

            users_id = ''.join(argss).replace('https://vk.com/', '')
            user = vk.method('users.get', {'user_ids': users_id, 'fields': 'friend_status'})
            name = user[0]['first_name']
            user_id = user[0]['id']
            user_id = int(user_id)

            vk.method('messages.addChatUser', {'chat_id': chat_id, 'user_id': user_id})
            messages.write_msg(peer_id, f"Пользователь @id{user_id}({name}) добавлен!")


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
