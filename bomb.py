import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import re
import asyncio
import json

def write_msg(peer_id, message, time):
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(0, 2048), 'disable_mentions': 1, 'expire_ttl': time})

def edit_msg(peer_id, message, msg_id):
    vk.method('messages.edit', {'peer_id': peer_id, 'message': message, 'message_id': msg_id})

def edita_msg(peer_id, message, attachments, msg_id):
    vk.method('messages.edit', {'peer_id': peer_id, 'message': message, 'attachment': attachments, 'message_id': msg_id})

def delete_msg(msg_id: int):
    vk.method("messages.delete", {'message_ids': msg_id, 'delete_for_all': 1})

async def bomb(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н сб" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = history['items'][0]['id']
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
        else:
            commands = args[0].lower()
            argss = args[1:]
        
        msg_1 = ''.join(payload)
        print(''.join(argss))
        try:
            time = ''.join(argss)
            time = int(time)
        except: 
                arg =  ''.join(argss)
                print(arg)
                time = int(''.join(arg[:-1]))
                arg = ''.join(arg[-1:])
                print(arg)
                if arg == 'ч':
                    time *= 3600
                if arg == 'м':
                    time *= 60
                if time > 86400:
                    write_msg("Выберете время меньше 24 часов")
        	
        write_msg(peer_id, msg_1, time)

        vk.method("messages.delete", {'message_ids': msg_id, 'delete_for_all': 1})

with open("database_token.json", "r", encoding="utf-8") as file:
   data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait = 0)

