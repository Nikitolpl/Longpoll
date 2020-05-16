import asyncio
import json
import re
import time

import vk_api
from vk_api.longpoll import VkLongPoll

from tools.messages import messages


def attachments(peer_id):
    history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})

    attachments = []
    for attachment in history['items'][0]['attachments']:
        a_type = attachment['type']
        if a_type in ['link']:
            continue
        attachments.append(
            f"{a_type}{attachment[a_type]['owner_id']}_{attachment[a_type]['id']}_{attachment[a_type]['access_key']}"
        )

    return attachments


async def create_templates(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н +ш" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            argss = args[1:]

            name = " ".join(argss)
            data_msg = payload
            attachment = attachments(peer_id)
            prov = 1

            if data_msg == "" and attachment == []:
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_temp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']
                print(data_temp)
                data_templ = {
                    "name": name,
                    "payload": data_msg,
                    "attachments": attachment
                }
                print(data_temp)
                data_temp.append(data_templ)
                print(data)
                data = {"templates": data_temp}
                with open("../database/database_lp_temp.json", "w", encoding="utf-8") as file:
                    file.write(json.dumps(data, ensure_ascii=False, indent=4))

                messages.write_msg(peer_id, f"""✅ Шаблон "{name}" сохранен. """)


async def templates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н мш" in command:
        with open("../database/database_lp_temp.json", "r", encoding="utf-8") as file:
            data = json.loads(file.read())
        data_temp = data['templates']

        _message = "📃Шаблоны дежурного:"
        itr = 0
        for temp in data_temp:
            itr += 1
            _message += f"\n{itr}. {temp['name']}"

        messages.write_msg(peer_id, _message)


async def one_templates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н ш" in command:
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            prov = 1

            if name == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_temp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']

                for temp in data_temp:
                    if temp['name'] == name:
                        messages.edita_msg(peer_id, temp['payload'], ",".join(temp['attachments']), msg_id)


async def delete_templates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н -ш" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)

            with open("../database/database_lp_temp.json", "r", encoding="utf-8") as file:
                data = json.loads(file.read())
            data_temp = data['templates']
            prov = 0

            for temp in data_temp:
                if temp['name'] == name:
                    data_temp.remove(temp)

                    data = {"templates": data_temp}
                    with open("../database/database_lp_temp.json", "w", encoding="utf-8") as file:
                        file.write(json.dumps(data, ensure_ascii=False, indent=4))

                    messages.write_msg(peer_id, f"""✅ Шаблон "{name}" удалён. """)
                    prov = 1
                    continue

            if prov == 0:
                messages.write_msg(peer_id, f'''❗ шаблон "{name}" не найден''')


# database_lp_dtemp.json

async def create_dtemplates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н +дш" in command:
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            data_msg = payload
            prov = 1

            if data_msg == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']
                print(data_temp)

                prov = 1
                for temp in data_temp:
                    if temp['name'] == name:
                        temp['payload'].append(data_msg)
                        print(data_temp)
                        data = {"templates": data_temp}
                        with open("../database/database_lp_dtemp.json", "w", encoding="utf-8") as file:
                            file.write(json.dumps(data, ensure_ascii=False, indent=4))

                        messages.write_msg(peer_id, f"""✅ В дшаб "{name}" был добавлен новый элемент. """)
                        prov = 0

                if prov == 1:
                    data_templ = {
                        "name": name,
                        "payload": [data_msg]
                    }
                    print(data_temp)
                    data_temp.append(data_templ)
                    print(data)
                    data = {"templates": data_temp}
                    with open("../database/database_lp_dtemp.json", "w", encoding="utf-8") as file:
                        file.write(json.dumps(data, ensure_ascii=False, indent=4))

                    messages.write_msg(peer_id, f"""✅ Шаблон "{name}" сохранен. """)


async def dtemplate(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н дш" in command:
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            prov = 1

            if name == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']

                for temp in data_temp:
                    if temp['name'] == name:
                        for i in range(len(temp['payload'])):
                            messages.edit_msg(peer_id, temp['payload'][i], msg_id)
                            time.sleep(1)


async def red_dtemplates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н рдш" in command:
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            data_msg = payload
            prov = 1

            if name == "" or data_msg == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']

                prov = 0
                for temp in data_temp:
                    if temp['name'] in name:
                        name_int = name.replace(str(temp['name']) + ' ', '')
                        print(name)
                        name_int = int(name_int)
                        name_int = name_int - 1
                        temp['payload'].insert(name_int, data_msg)
                        name_in = name_int + 1
                        temp['payload'].pop(name_in)
                        print(data_temp)
                        data = {"templates": data_temp}
                        with open("../database/database_lp_dtemp.json", "w", encoding="utf-8") as file:
                            file.write(json.dumps(data, ensure_ascii=False, indent=4))

                        messages.write_msg(peer_id, f"""✅ В дшаб "{temp['name']}" был изменён элемент. """)
                        prov = 1
                        break

                if prov == 0:
                    messages.write_msg(peer_id, f"""❗ Элемент не был найден!""")


async def dele_dtemplates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н удш" in command:
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            prov = 1

            if name == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']

                prov = 0
                for temp in data_temp:
                    if temp['name'] in name:
                        name_int = name.replace(str(temp['name']) + ' ', '')
                        print(name)

                        try:
                            name_int = int(name_int)
                            name_int = name_int - 1
                        except:
                            messages.write_msg(peer_id, f"""❗ Элемент не был найден!""")
                            prov = 1
                            break

                        temp['payload'].pop(name_int)
                        print(data_temp)
                        data = {"templates": data_temp}
                        with open("../database/database_lp_dtemp.json", "w", encoding="utf-8") as file:
                            file.write(json.dumps(data, ensure_ascii=False, indent=4))

                        messages.write_msg(peer_id, f"""✅ В дшаб "{temp['name']}" был удалён элемент. """)
                        prov = 1
                        break

                if prov == 0:
                    messages.write_msg(peer_id, f"""❗ Элемент не был найден!""")


async def dtemplates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н мдш" in command:
        with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
            data = json.loads(file.read())
        data_temp = data['templates']

        _message = "📃Дшабы дежурного:"
        itr = 0
        for temp in data_temp:
            itr += 1
            _message += f"\n{itr}. {temp['name']}"

        messages.write_msg(peer_id, _message)


async def dtemplates_temp(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н эдш" in command:
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            prov = 1

            if name == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']

                _message = f"📃Элементы дшаба \"{name}\":"
                itr = 0
                for temp in data_temp:
                    if temp['name'] in name:
                        for i in range(len(temp['payload'])):
                            itr += 1
                            _message += f"\n{itr}. {temp['payload'][i]}"

                messages.write_msg(peer_id, _message)


async def delete_dtemplates(delay, peer_id, command) -> str:
    await asyncio.sleep(delay)
    if "!н -дш" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
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
            messages.write_msg(peer_id, "❗ Нет данных")

        else:
            commands = args[0].lower()
            argss = args[1:]

            name = " ".join(argss)
            prov = 1

            if name == "":
                messages.write_msg(peer_id, "❗ Нет данных")
                prov = 0

            if prov == 1:
                with open("../database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
                    data = json.loads(file.read())
                data_temp = data['templates']

                for temp in data_temp:
                    if temp['name'] == name:
                        data_temp.remove(temp)

                        data = {"templates": data_temp}
                        with open("../database/database_lp_dtemp.json", "w", encoding="utf-8") as file:
                            file.write(json.dumps(data, ensure_ascii=False, indent=4))

                        messages.write_msg(peer_id, f"""✅ Шаблон "{name}" удалён. """)
                        prov = 1
                        continue

                if prov == 0:
                    messages.write_msg(peer_id, f'''❗ шаблон "{name}" не найден''')


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
