import asyncio
import json
import time

import vk_api
from vk_api.longpoll import VkLongPoll

from tools.messages import messages
from tools.requests import vk_info


async def BFanim_info(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н дшабы" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        msg_1 = f"""
            Список дшабов:
            1. таймер
            2. луна
            3. бомба
            4. зарплата
            5. выстрел
            6. поцеловать
            7. бух
            8. нахуй
            9. накормить
            10. пожалуйста
            11. хатьфу
            12. убить
            13. письмо
            14. привет
            15. пока
            16. вселенная
            17. свидание
            18. пнуть
            19. ударить
            20. брак
            21. кекс
            22. ъуъ
            """.replace('    ', '')
        messages.edit_msg(peer_id, msg_1, msg_id)
        time.sleep(1)


async def BFanim(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н таймер" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            '🔟',
            '9️⃣',
            '8️⃣',
            '7️⃣',
            '6️⃣',
            '5️⃣',
            '4️⃣',
            '3️⃣',
            '2️⃣',
            '1️⃣',
            '✅ Время вышло ✅',
        ]

        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim1(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н луна" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = '🌑🌒🌓🌔🌕🌖🌗🌘'
        for i in range(9):
            messages.edit_msg(peer_id, pic, msg_id)
            pic = pic[-1:] + pic[:-1]
            time.sleep(1)


async def BFanim2(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н бомба" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            '😠        😝',
            '😡        😝',
            '😡👉💣     😝',
            '😡 👉💣   😝',
            '😡  👉💣   😝',
            '😡   👉💣  😝',
            '😡    👉💣 😝',
            '😡     👉💣😝',
            '😌     👉💣💀'
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim3(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н зарплата" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😔     🙋‍♂",
            "😔     💁‍♂💵",
            "😔    💵💁‍♂",
            "😔   💵💁‍♂",
            "😔  💵💁‍♂",
            "😔 💵💁‍♂",
            "😔💵💁‍♂",
            "😔💵🙋‍♂",
            "😦💵",
            "😁💵"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim4(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н выстрел" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😏 😣",
            "😂 🔫😡",
            "😨 • 🔫😡",
            "😵💥 🔫😡"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim5(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н поцеловать" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😺     🙄",
            "😺    🙄",
            "😺   🙄",
            "😺  🙄",
            "😺 🙄",
            "😺🙄",
            "😽😍"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim6(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н бух" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😋    🍾",
            "😄   🍾",
            "😁  🍾",
            "🤤 🍾",
            "🤢",
            "🤮"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim7(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н нахуй" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😔      🤣",
            "😡    🤣",
            "😡 🖕    🤣",
            "😏     😢",
            "🤣     😭"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim8(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н накормить" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "🤔     😒",
            "🤔🍔    😒",
            "😊 🍔   😒",
            "😊  🍔  😲",
            "😊   🍔 😲",
            "😁    🍔🤤",
            "😌🍔😋"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim9(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н пожалуйста" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "🤓     🤔",
            "🤓    🚶",
            "🤓   🚶",
            "🤓  😦",
            "🤓 🚶",
            "🤓🤔",
            "🗣😏",
            "🤝"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim10(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н хатьфу" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "🙂      🙂",
            "😦      🙂",
            "😯      🙂",
            "😗💦     🙂",
            "😗 💦    🙂",
            "😗  💦   🤔",
            "😗   💦  😳",
            "😁    💦 😦",
            "😂     💦😪",
            "😈      😵"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim11(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н убить" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "🙁     😎",
            "😤     😎",
            "😡🔪    😎",
            "😡 🔪   😯",
            "😡  🔪  😧",
            "😡   🔪 😧",
            "😡    🔪😩",
            "😁     😵"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim12(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н письмо" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😊💬         😔",
            "😊  💬       😔",
            "😊    💬     😔",
            "😊      💬   😔",
            "😊         💬😔",
            "😊         😃"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim13(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н пока" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😁🖐 ",
            "😐👋 ",
            "😕🖐 ",
            "😔👋 ",
            "😔✋ ",
            "😔👋 ",
            "😔✋"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim14(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н привет" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😄🖐",
            "😄👋",
            "😄🖐",
            "😄👋",
            "😄🖐",
            "😄👋"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim15(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н вселенная" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "🌑✨✨🌏✨✨✨",
            "✨🌑✨🌍✨✨✨",
            "✨✨🌑🌎✨✨✨",
            "✨✨✨🌏🌕✨✨",
            "✨✨✨🌍✨🌕✨",
            "✨✨✨🌎✨✨🌕"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim16(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н свидание" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "💃    🕺",
            " 💃  🕺 ",
            "  💃🕺  ",
            "  👫 🌇",
            "   👫🌇",
            "   💑🌇",
            "   💏🌇"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim17(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н пнуть" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😑👟     🤔",
            "😑 👟    🤔",
            "😑  👟   🤔",
            "😑   👟  🤔",
            "😑    👟 🤔",
            "😏     👟🤕"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim18(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н ударить" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😔     🤣",
            "😤     😂",
            "😡🤜    🤣",
            "😡 🤜   😂",
            "😡  🤜  🤣",
            "😡   🤜 🤣",
            "😡    🤜😣",
            "😌     😵"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim19(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н брак" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "🙋   🏃",
            "💁💕  🚶",
            "🙎  🎁🙇",
            "🙎🎁  🙇",
            "🙆💍 🎁🙇",
            " 💕💏💕",
            "💕 💑 💕",
            "👫   ⛪",
            "👫  ⛪",
            "👫 ⛪",
            "👫💒"
        ]
        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim20(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н кекс" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        pic = [
            "😶     😶",
            "😍     😍",
            "😍👉   👌😍",
            "😍 👉 👌 😍",
            "😍  👉👌 😍",
            "😍 👉 👌 😍",
            "🤤     🤤"
        ]

        for i in range(len(pic)):
            messages.edit_msg(peer_id, pic[i], msg_id)
            time.sleep(1)


async def BFanim21(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н ъуъ" in command:
        msg_id = vk_info.info_msg_id(peer_id)
        picl = [
            '🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕', '🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕', '🌘🌑🌕🌕🌘🌑🌒🌕🌕🌕',
            '🌑🌕🌕🌘🌑🌑🌑🌓🌕🌕', '🌘🌔🌖🌑👁🌑👁🌓🌗🌒', '🌖🌓🌗🌑🌑🌑🌑🌔🌕🌑',
            '🌕🌗🌑🌑🌑🌑🌒🌕🌘🌒', '🌕🌕🌘🌑🌑🌑🌑🌑🌒🌕', '🌕🌕🌘🌑🌑🌑🌔🌕🌕🌕',
            '🌕🌕🌘🌔🌘🌑🌕🌕🌕🌕', '🌕🌖🌒🌕🌗🌒🌕🌕🌕🌕', '🌕🌗🌓🌕🌗🌓🌕🌕🌕🌕']
        pic0 = picl[0]
        pic1 = picl[1]
        pic2 = picl[2]
        pic3 = picl[3]
        pic4 = picl[4]
        pic5 = picl[5]
        pic6 = picl[6]
        pic7 = picl[7]
        pic8 = picl[8]
        pic9 = picl[9]
        pic10 = picl[10]
        pic11 = picl[11]

        for i in range(11):
            messages.edit_msg(peer_id,
                              f"""{pic0}\n{pic1}\n{pic2}\n{pic3}\n{pic4}\n{pic5}\n{pic6}\n{pic7}\n{pic8}\n{pic9}\n{pic10}\n{pic11}""",
                              msg_id)
            pic0 = pic0[-1:] + pic0[:-1]
            pic1 = pic1[-1:] + pic1[:-1]
            pic2 = pic2[-1:] + pic2[:-1]
            pic3 = pic3[-1:] + pic3[:-1]
            pic4 = pic4[-1:] + pic4[:-1]
            pic5 = pic5[-1:] + pic5[:-1]
            pic6 = pic6[-1:] + pic6[:-1]
            pic7 = pic7[-1:] + pic7[:-1]
            pic8 = pic8[-1:] + pic8[:-1]
            pic9 = pic9[-1:] + pic9[:-1]
            pic10 = pic10[-1:] + pic10[:-1]
            pic11 = pic11[-1:] + pic11[:-1]
            time.sleep(0.8)


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']
# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
