from tools.messages import messages
from tools.requests import vk_info
import vk_api
from vk_api.longpoll import VkLongPoll
import re
import asyncio
import time
import random
import json

start = False


def add_friend(user_id):
    vk.method('friends.add', {'user_id': user_id})


def del_friend(user_id):
    vk.method('friends.delete', {'user_id': user_id})


async def add_friends(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н +др" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = history['items'][0]['conversation_message_id']
        msg_text = history['items'][0]['text']

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

            history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
            user_id = history['items'][0]['reply_message']['from_id']
            print(user_id)
            user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status'})
            name = user[0]['first_name']
            friend = user[0]['friend_status']
            friends = int(friend)
            user_ids = "id" + str(user_id)

        else:
            commands = args[0].lower()
            argss = args[1:]

            user_id = ''.join(argss).replace('https://vk.com/', '')
            print(user_id)
            user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status'})
            user_id = user[0]['id']
            print(user_id)
            name = user[0]['first_name']
            friend = user[0]['friend_status']
            friends = int(friend)
            user_ids = "id" + str(user_id)
        if friends == 0:
            add_friend(user_id)

            msg_1 = f"""
            Заявка отправлена пользователю: @{user_ids}({name})
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)
        elif friends == 1:

            msg_1 = f"""
            Заявка пользователю @{user_ids}({name}) уже отправлена.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)
        elif friends == 2:
            add_friend(user_id)

            msg_1 = f"""
            Заявка в друзья от пользователя @{user_ids}({name}) принята.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)
        else:

            msg_1 = f"""
            Пользователь @{user_ids}({name}) уже в друзьях.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)


async def del_friends(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н -др" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = history['items'][0]['conversation_message_id']
        msg_text = history['items'][0]['text']

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

            history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
            user_id = history['items'][0]['reply_message']['from_id']
            user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status'})
            name = user[0]['first_name']
            friend = user[0]['friend_status']
            friends = int(friend)
            users_id = "id" + str(user_id)

        else:
            commands = args[0].lower()
            argss = args[1:]

            user_id = ''.join(argss).replace('https://vk.com/', '')
            print(user_id)
            user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status'})
            user_id = user[0]['id']
            name = user[0]['first_name']
            friend = user[0]['friend_status']
            friends = int(friend)
            users_id = "id" + str(user_id)

        if friend == 0:

            msg_1 = f"""
            Пользователь @{users_id}({name}) нет в списке друзей.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)

        elif friends == 1:
            del_friend(user_id)

            msg_1 = f"""
            Заявка пользователю @{users_id}({name}) удалена.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)
        elif friends == 2:
            del_friend(user_id)

            msg_1 = f"""
            Заявка в друзья от пользователя @{users_id}({name}) не принята.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)
        else:
            del_friend(user_id)

            msg_1 = f"""
            Пользователь @{users_id}({name}) удалён из друзей.
            """.replace('    ', '')

            messages.write_msg(peer_id, msg_1)


async def add_friends_conversations(delay, peer_id, command):
    user_id = vk.method('users.get', {})
    user_id = user_id[0]['id']
    await asyncio.sleep(delay)
    if "!н +дрв" in command:
        msg_text = vk_info.info_msg_text(peer_id)
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
            messages.write_msg(peer_id, "❗Укажите кол-во секунд перед добавлением в друзья")
        else:
            commands = args[0].lower()
            argss = args[1:]

            count = ''.join(argss)
            count = int(count)
            count_1 = count + 2
            count_2 = count - 2
            count_3 = count + 3
            count_4 = count - 3
            counts = [count, count_1, count_2, count_3, count_4]
            messages.write_msg(peer_id, "...Начинаю добавлять всю беседу в друзья...")
            members_friend = []
            for members in vk_info.all_members(peer_id):
                if members['member_id'] < 0:
                    print("Невозможно добавить группу в др")
                elif members['member_id'] == user_id:
                    print("Невозможно добавить себя в др")
                elif members['member_id'] > 0:
                    members_friend.append(str(members['member_id']))
            for i in range(len(members_friend)):
                try:
                    print(members_friend[i])
                    add_friend(members_friend[i])
                    time.sleep(random.choice(counts))
                    if command == "!н -дрв":
                        messages.write_msg(peer_id, "✅ Добавление всей беседы в друзья отключенно")
                        continue
                except:
                    print("Пользователь заморожен")

            messages.write_msg(peer_id, "✅ Все участники беседы добавленны!")


async def auto_add_friends_on(delay, command):
    await asyncio.sleep(delay)
    global start
    if "!н +адвд" in command:
        start = True


async def auto_add_friends(delay, peer_id, command):
    await asyncio.sleep(delay)
    global start
    if "!н +адвд" in command:
        messages.write_msg(peer_id, "✅ Автодобавление в друзья включенно")
        while start:
            data: dict = vk.method('friends.getRequests',
                                   {'offset': 0, 'count': 1000, 'extended': 0,
                                    'need_mutual': 0, 'out': 0, 'need_viewed': 1})['items']
            print(data)
            users: dict = vk.method('users.get', {'user_ids': ",".join([str(i) for i in data])})
            for user in users:
                if None != user.get('deactivated', None):
                    print("Невозможно добавить забаненого пользователя в друзья")
                    continue
                try:
                    vk.method("friends.add", {'user_id': user['id']})
                    print("Добавлен: " + str(user['id']))
                except:
                    print("Ошибка при добавлении в друзья")
                time.sleep(5)
            time.sleep(300)


async def auto_add_friends_off(delay, peer_id, command):
    await asyncio.sleep(delay)
    global start
    if "!н -адвд" in command:
        start = False
        messages.write_msg(peer_id, "✅ Автодобавление в друзья отключено!")


def auto_add_friends_info():
    global start
    if start:
        autofr = "✅"
    elif not start:
        autofr = "❌"
    return autofr


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
