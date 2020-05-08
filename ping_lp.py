import asyncio
import json
from typing import Any, Union

import vk_api
from vk_api.longpoll import VkLongPoll

import messages
import vk_info


async def ping_info(delay, peer_id, command):
    await asyncio.sleep(delay)
    if command == "!н пинг" or command == "!н пиу" or command == "!н кинг" or command == "!н п" or command == "!лгбт " \
                                                                                                              "пинг" \
            or command == "!гей пинг":
        delta: Union[float, Any] = vk_info.info_msg_date(peer_id)
        # c_time_str = str(datetime.fromtimestamp(round(c_time)))
        # v_time_str = str(datetime.fromtimestamp(round(event.msg['date'])))

        r_type = 'ПОНГ' if command == "!н пинг" else "ПАУ" if command == "!н пиу" else 'PONG' if command == "!н п" else\
            "ЛГБТ" if command == "!лгбт пинг" else "КТО ПРОЧИТАЛ ТОТ ГЕЙ" if command == "!гей пинг" else "КОНГ "

        if delta > 15:
            r_type += "\nlongpoll дежурный отвечает слишком долго!"
        elif delta > 10:
            r_type += "\nlongpoll дежурный работает с большой задержкой."
        elif delta > 5:
            r_type += "\nlongpoll дежурный работает не стабильно."
        else:
            r_type += "\nlongpoll дежурный работает"

        msg_1 = f"""{r_type}
        Ответ через: {delta} с.
        """.replace('    ', '')

        messages.write_msg(peer_id, msg_1)


with open("database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
