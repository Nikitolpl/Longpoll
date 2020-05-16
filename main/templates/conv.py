import asyncio
import json
import re

import vk_api
from vk_api.longpoll import VkLongPoll

from tools.messages import messages
from tools.requests import vk_info


async def fonts(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н шрифты" in command:
        messages.write_msg(peer_id, """
1. 𝕠𝕦𝕥𝕝𝕚𝕟𝕖 (outline)
2. 𝚝𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛 (typewriter)
3. 𝓈𝒸𝓇𝒾𝓅𝓉 (script)
4. 𝓼𝓬𝓻𝓲𝓹𝓽_𝓫𝓸𝓵𝓭 (script_bold)
5. zɾƃlɟq_ɟʞuʍ (upside_down)
6. ᴛɪɴʏ_ᴄᴀᴘs (tiny_caps)
7. ᑕOᗰIᑕ (comic)
8. 𝐬𝐞𝐫𝐢𝐟_𝐛 (serif_b)
9. 𝑠𝑒𝑟𝑖𝑓_𝑖 (serif_i)
10. 𝒔𝒆𝒓𝒊𝒇_𝒃𝒊 (serif_bi)
11. ⒸⒾⓇⒸⓁⒺⓈ (circles)
12. 🅒🅘🅡🅒🅛🅔🅢_🅑 (circles_b)
13. 🅂🅀🅄🄰🅁🄴🅂 (squares)
14. 𝔤𝔬𝔱𝔥𝔦𝔠 (gothic)
15. 𝖌𝖔𝖙𝖍𝖎𝖈_𝖇 (gothic_b)""")


async def font(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н пш" in command:
        history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        msg_id = vk_info.info_msg_id(peer_id)
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
            messages.edit_msg(peer_id, """
        Просмотр списка шрифтов - .с шрифты
        \nКоманда для конвертации:\n!н пш [номер]\n[текст]
        \n!Русские буквы игнорируются""", msg_id)

        else:
            commands = args[0].lower()
            argss = args[1:]
            count = ''.join(argss)
            msg_1 = ''.join(payload)
            alw = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
            if count == '1':
                dest = u"~!@#$%^&𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡[]𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝;'𝕫𝕩𝕔𝕧𝕓𝕟𝕞,./ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ{}𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃:\"|ℤ𝕏ℂ𝕍𝔹ℕ𝕄<>?"
            elif count == '2':
                dest = u"~!@#$%^&𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙[]𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕;'𝚣𝚡𝚌𝚟𝚋𝚗𝚖,./𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿{}𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻:\"|𝚉𝚇𝙲𝚅𝙱𝙽𝙺<>?"
            elif count == '3':
                dest = u"~!@#$%^&𝓆𝓌ℯ𝓇𝓉𝓎𝓊𝒾ℴ𝓅[]𝒶𝓈𝒹𝒻ℊ𝒽𝒿𝓀𝓁;'𝓏𝓍𝒸𝓋𝒷𝓃𝓂,./𝒬𝒲ℰℛ𝒯𝒴𝒰ℐ𝒪𝒫{}𝒜𝒮𝒟ℱ𝒢ℋ𝒥𝒦ℒ:\"|𝒵𝒳𝒞𝒱ℬ𝒩ℳ<>?"
            elif count == '4':
                dest = u"~!@#$%^&𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹[]𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵;'𝔃𝔁𝓬𝓿𝓫𝓷𝓶,./𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟{}𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛:\"|𝓩𝓧𝓒𝓥𝓑𝓝𝓜<>?"
            elif count == '5':
                dest = u"~¡@#$%^&ɯuqʌɔxzlʞɾ[]ɥƃɟpsɐdoᴉ;'nʎʇɹǝʍb,./ɯuqʌɔxzlʞɾ{}ʎƃɟpsɐdoᴉ:\"|nʎʇɹǝʍb<>¿"
            elif count == '6':
                dest = u"~!@#$%^&ǫᴡᴇʀᴛʏᴜɪᴏᴘ[]ᴀsᴅғɢʜᴊᴋʟ;'ᴢxᴄᴠʙɴᴍ,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
            elif count == '7':
                dest = u"~!@#$%^&ᑫᗯᗴᖇTYᑌIOᑭ[]ᗩՏᗪᖴᘜᕼᒍKᒪ;'ᘔ᙭ᑕᐯᗷᑎᗰ,./ᑫᗯᗴᖇTYᑌIOᑭ{}ᗩՏᗪᖴᘜᕼᒍKᒪ:\"|ᘔ᙭ᑕᐯᗷᑎᗰ<>?"
            elif count == '8':
                dest = u"~!@#$%^&𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩[]𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥;'𝐳𝐱𝐜𝐯𝐛𝐧𝐦,./𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏{}𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋:\"|𝐙𝐗𝐂𝐕𝐁𝐍𝐌<>?"
            elif count == '9':
                dest = u"~!@#$%^&𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝[]𝑎𝑠𝑑𝑓𝑔ℎ𝑗𝑘𝑙;'𝑧𝑥𝑐𝑣𝑏𝑛𝑚,./𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃{}𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿:\"|𝑍𝑋𝐶𝑉𝐵𝑁𝑀<>?"
            elif count == '10':
                dest = u"~!@#$%^&𝒒𝒘𝒆𝒓𝒕𝒚𝒖𝒊𝒐𝒑[]𝒂𝒔𝒅𝒇𝒈𝒉𝒋𝒌𝒍;'𝒛𝒙𝒄𝒗𝒃𝒏𝒎,./𝑸𝑾𝑬𝑹𝑻𝒀𝑼𝑰𝑶𝑷{}𝑨𝑺𝑫𝑭𝑮𝑯𝑱𝑲𝑳:\"|𝒁𝑿𝑪𝑽𝑩𝑵𝑴<>?"
            elif count == '11':
                dest = u"~!@#$%^&ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ[]ⒶⓈⒹⒻⒼⒽⒿⓀⓁ;'ⓏⓍⒸⓋⒷⓃⓂ,./ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ{}ⒶⓈⒹⒻⒼⒽⒿⓀⓁ:\"|ⓏⓍⒸⓋⒷⓃⓂ<>?"
            elif count == '12':
                dest = u"~!@#$%^&🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟[]🅐🅢🅓🅕🅖🅗🅙🅚🅛;'🅩🅧🅒🅥🅑🅝🅜,./🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟{}🅐🅢🅓🅕🅖🅗🅙🅚🅛:\"|🅩🅧🅒🅥🅑🅝🅜<>?"
            elif count == '13':
                dest = u"~!@#$%^&🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿[]🄰🅂🄳🄵🄶🄷🄹🄺🄻;'🅉🅇🄲🅅🄱🄽🄼,./🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿{}🄰🅂🄳🄵🄶🄷🄹🄺🄻:\"|🅉🅇🄲🅅🄱🄽🄼<>?"
            elif count == '14':
                dest = u"~!@#$%^&𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭[]𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩;'𝔷𝔵𝔠𝔳𝔟𝔫𝔪,./𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓{}𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏:\"|ℨ𝔛ℭ𝔙𝔅𝔑𝔐<>?"
            elif count == '15':
                dest = u"~!@#$%^&𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕[]𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑;'𝖟𝖝𝖈𝖛𝖇𝖓𝖒,./𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻{}𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷:\"|𝖅𝖃𝕮𝖁𝕭𝕹𝕸<>?"

            fonts = dict(zip(alw, dest))
            s = msg_1
            msg = u''.join([fonts.get(c, c) for c in s])
            messages.edit_msg(peer_id, msg, msg_id)


async def convert(delay, peer_id, command):
    await asyncio.sleep(delay)
    if "!н конв" in command:
        msg_text = vk_info.info_msg_text(peer_id)
        _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
        _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
        _trans_table = dict(zip(_eng_chars, _rus_chars))

        s = ''
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
            try:
                history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
                reply_message = history['items'][0]['reply_message']['text']
                s = s + '\n' + reply_message
            except:
                print("Данных не обноруженно!")
        else:
            commands = args[0].lower()
            argss = args[1:]

            if bool(argss):
                s = " ".join(argss)
            if bool(payload):
                s = s + '\n' + payload
        if s == "":
            messages.write_msg(peer_id, 'Нет данных 🤦')
        else:
            msg = u''.join([_trans_table.get(c, c) for c in s])
            messages.write_msg(peer_id, msg)


with open("main/database/database_token.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())
token = data['token']
# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait=0)
