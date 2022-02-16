import asyncio , telethon , logging , time , random , os , html
from telethon import utils
from telethon import client
from telethon import events 
from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
Download_path = './DOWNLOAD/'

feri = 'BAAK-xvePWLi5TaQwYKSHX249UsL1ptjmQke25WiSk5SXJr18ANYsNxQ38ZndswDUovazfrgjmjHpvEmIrqdpmx2xjqU-sMMYs4LJ1Rl2Tb4Fwb8I62v_lPzjjSqTvCulshrMxkQQmhfccGMks-eyqGtWMWsgE9tL4GhitgIGdXtcVwdUZz9oEcy-u8CE2cYcrnZCVtmHOmvGD_bh8P1t8atYVstIKbo7B69FbFsTFRQYCXyiNa95mDcroLCAHOAS-wsUPiwMMM89VAI-cGwNBAa3uvA4iHzrd9F6Tp6xnCd8IYqE2XjKZNaF2VOvBpcm5PgbI_OQ7sAaf_tJjJ9uWWUAAAAATuwAm0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

@client.on(events.NewMessage(pattern=r"\.say (.*)", outgoing=True))
async def SAY(event):
    if event.fwd_from:
        return
    
    input_str = event.pattern_match.group(1)
    typing_symbol = "|"
    DELAY_BETWEEN_EDITS = 0.1
    previous_text = ""
    await event.edit(typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        await event.edit(typing_text)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        await event.edit(previous_text)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)




        
        
@client.on(events.NewMessage(pattern=r"\.react (.*)", outgoing=True))
async def RANDOMreact(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "happy":
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "(ʘ‿ʘ)",
            "(✿´‿`)",
            "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
            "(*⌒▽⌒*)θ～♪",
            "°˖✧◝(⁰▿⁰)◜✧˖°",
            "✌(-‿-)✌",
            "⌒°(❛ᴗ❛)°⌒",
            "(ﾟ<|＼(･ω･)／|>ﾟ)",
            "ヾ(o✪‿✪o)ｼ",
        ]
    elif input_str in "thinking":
        emoticons = [
            "(҂⌣̀_⌣́)",
            "（；¬＿¬)",
            "(-｡-;",
            "┌[ O ʖ̯ O ]┐",
            "〳 ͡° Ĺ̯ ͡° 〵",
        ]
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪`◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ`)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀̿Ĺ̯▀̿ ̿)",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)





@client.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def OSinfo(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "macos":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Hackintosh...`",
            "`Initiating Hackintosh Login.`",
            "`Loading Hackintosh... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Hackintosh... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Hackintosh... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Hackintosh... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Hackintosh... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Hackintosh... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Hackintosh... 89%\n█████████████████████▒▒▒▒ `",
            "`Loading Hackintosh... 100%\n█████████████████████████ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Hackintosh`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@client.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def OSinfo(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "windows":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Windows 10...`",
            "`Initiating Windows 10 Login.`",
            "`Loading Windows 10... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Windows 10... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 89%\n█████████████████████▒▒▒▒ `",
            "`Loading Windows 10... 100%\n█████████████████████████ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])



@client.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def OSinfo(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "linux":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Linux...`",
            "`Initiating Linux Login.`",
            "`Loading Linux... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Linux... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 89%\n█████████████████████▒▒▒▒ `",
            "`Loading Linux... 100%\n█████████████████████████ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@client.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def OSinfo(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "stock":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Symbian OS...`",
            "`Initiating Symbian OS Login.`",
            "`Loading Symbian OS... 0%\n█████████████████████████ `",
            "`Loading Symbian OS... 3%\n█████████████████████▒▒▒▒ `",
            "`Loading Symbian OS... 9%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Symbian OS... 23%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 39%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 69%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 89%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 100%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@client.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def OSinfo(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 7)

    input_str = event.pattern_match.group(1)

    if input_str == "os":

        await event.edit(input_str)

        animation_chars = [
        
            "`Scanning OS...`",
            "`Scanning OS......`",
            "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n☑️ `.macos`\n☑️ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
            "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n☑️ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
            "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n✅ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
            "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n✅ `.windows`\n✅ `.linux`\n☑️ `.stock`",
            "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\n✅ `.macos`\n✅ `.windows`\n✅ `.linux`\n✅ `.stock`\n\nDeveloped By: @CyberProgram"
 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 7])
            


            
import aiohttp
import io
import time
from datetime import tzinfo, datetime

mapid = '1312815a8d5a3338c39e1c671dbd4315'
@client.on(events.NewMessage(pattern=".weather (.*)"))
async def wheather(event):
    if event.fwd_from:
        return
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str, mapid))
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await event.reply(
            """{}
**میزان درجه هوا**: {}°С
    __کمترین درجه__: {}°С
    __بالاترین درجه__ : {}°С
**مرطوبیت**: {}%
**درجه باد بر مایل**: {}m/s
**ابر**: {}hpa
**طلوع افتاب**: {} {}
**غروب افتاب**: {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                country_code
            )
        )








import html
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

@client.on(events.NewMessage(pattern=r"\.info ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    replied_user_profile_photos = await client(GetUserPhotosRequest(
        user_id=replied_user.user.id,
        offset=42,
        max_id=0,
        limit=80
    ))
    replied_user_profile_photos_count = "NaN"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError as e:
        pass
    user_id = replied_user.user.id
    first_name = html.escape(replied_user.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    last_name = last_name.replace(
        "\u2060", "") if last_name else ("Last Name not found")
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "`Need a Profile Picture to check **this**`"
        location = str(e)
    caption = """<b>Extracted by MHMOFFICIAL<b>
<b>🔥Telegram ID</b>: <code>{}</code>
<b>🤟Permanent Link</b>: <a href='tg://user?id={}'>Click Here</a>
<b>🗣️First Name</b>: <code>{}</code>
<b>🗣️Second Name</b>: <code>{}</code>
<b>👨🏿‍💻BIO</b>: {}
<b>🎃DC ID</b>: {}
<b>⚡NO OF PSS</b> : {}
<b>🤔IS RESTRICTED</b>: {}
<b>✅VERIFIED</b>: {}
<b>🙄IS A BOT</b>: {}
<b>👥Groups in Common</b>: {}
""".format(
        user_id,
        user_id,
        first_name,
        last_name,
        user_bio,
        dc_id,
        replied_user_profile_photos_count,
        replied_user.user.restricted,
        replied_user.user.verified,
        replied_user.user.bot,
        common_chats
    )
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = event.message.id
    await client.send_message(
        event.chat_id,
        caption,
        reply_to=message_id_to_reply,
        parse_mode="HTML",
        file=replied_user.profile_photo,
        force_document=False,
        silent=True
    )
    await event.delete()


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e










from telethon.tl.types import ChannelParticipantsAdmins
@client.on(events.NewMessage(pattern=r"\.tagall ?(.*)", outgoing=True))
async def tagall(event):
    if event.fwd_from:
        return
    mentions = "⚡️اخرین افراد انلاین گروه⚡️"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@client.on(events.NewMessage(pattern=r"\.tagadmin ?(.*)", outgoing=True))
async def tagadmin(event):
    if event.fwd_from:
        return
    mentions = "Admins : "
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()








import os
import time
import math
import asyncio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from telethon.tl.types import DocumentAttributeAudio


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

@client.on(events.NewMessage(pattern=".yt(a|v) (.*)"))
async def download_video(v_url):
    """ For .ytdl command, download media from YouTube and many other sites. """
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()

    await v_url.edit("`Preparing to download...`")

    if type == "a":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '480',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True

    try:
        await v_url.edit("`درحال گرفتن اطلاعات لطفا صبر کنید ...`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await v_url.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v_url.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await v_url.edit(
            "`به دلیل محدودیت های جغرافیایی اعمال شده توسط یک وب سایت، ویدیو در موقعیت جغرافیایی شما در دسترس نیست ساده تر بگم فیلتر شکن نصب کنیدبه دلیل محدودیت های جغرافیایی اعمال شده توسط یک وب سایت، ویدیو در موقعیت جغرافیایی شما در دسترس نیست ساده تر بگم فیلتر شکن نصب کنید.`"
        )
        return
    except MaxDownloadsReached:
        await v_url.edit("`حداکثر تعداد دانلود به حد مجاز رسیده است.")
        return
    except PostProcessingError:
        await v_url.edit("`در حین پردازش پست خطایی روی داد.`")
        return
    except UnavailableVideoError:
        await v_url.edit("`رسانه در قالب درخواستی موجود نیست.`")
        return
    except XAttrMetadataError as XAME:
        await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v_url.edit("`در حین پردازش پست خطایی روی داد.")
        return
    except Exception as e:
        await v_url.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await v_url.edit(f"`در حال اپلود موزیک:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(ytdl_data['duration']),
                                       title=str(ytdl_data['title']),
                                       performer=str(ytdl_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{ytdl_data['title']}.mp3")))
        os.remove(f"{ytdl_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await v_url.edit(f"` درحال اپلود موزیک ویدیو:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            supports_streaming=True,
            caption=ytdl_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{ytdl_data['title']}.mp4")))
        os.remove(f"{ytdl_data['id']}.mp4")
        await v_url.delete()







from telethon import events
from telethon.tl import functions



@client.on(events.NewMessage(pattern=".pbio (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            about=bio
        ))
        await event.edit("بیوگرافی شما با موفقیت تعغیر کرد")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@client.on(events.NewMessage(pattern=".pname ((.|\n)*)"))  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            first_name=first_name,
            last_name=last_name
        ))
        await event.edit("اسم شما با موفقیت تعغییر کرد")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))



@client.on(events.NewMessage(pattern=".ppic"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("درحال دانلود پروفایل در لوکال ...")
    if not os.path.isdir(Download_path):  # pylint:disable=E0602
        os.makedirs(Download_path)  # pylint:disable=E0602
    photo = None
    try:
        photo = await client.download_media(  # pylint:disable=E0602
            reply_message,
            Download_path  # pylint:disable=E0602
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("درحال اپلود به @Telegram ...")
            file = await client.upload_file(photo)  # pylint:disable=E0602
            try:
                await client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                    file
                ))
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("پروفایل با موفقیت عوض شد ☑")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602






import subprocess
from datetime import datetime
from gtts import gTTS



@client.on(events.NewMessage(pattern=".voice (.*)"))
async def Voice(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("شما به طور اشتباه دستور را وارد کردید.")
        return
    text = text.strip()
    lan = lan.strip()
    if not os.path.isdir(Download_path):
        os.makedirs(Download_path)
    required_file_name = Download_path + "voice.ogg"
    try:
        #https://github.com/SpEcHiDe/Uniclient/commit/17f8682d5d2df7f3921f50271b5b6722c80f4106
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        try:
            t_response = subprocess.check_output(command_to_execute, stderr=subprocess.STDOUT)
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await event.edit(str(exc))
            # continue sending required_file_name
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await client.send_file(
            event.chat_id,
            required_file_name,
            # caption="Processed {} ({}) in {} seconds!".format(text[0:97], lan, ms),
            reply_to=event.message.reply_to_msg_id,
            allow_cache=False,
            voice_note=True
        )
        os.remove(required_file_name)
        await event.edit("پروسس در {} ({}) in {} انجام شد !".format(text[0:97], lan, ms))
        await asyncio.sleep(5)
        await event.delete()
    except Exception as e:
        await event.edit(str(e))



logger = logging.getLogger(__name__)
DEL_TIME_OUT = 60
from telethon.errors import FloodWaitError
@client.on(events.NewMessage(pattern=".bioclock"))  # pylint:disable=E0602
async def bioclock(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | I am A Pro 😎 | ⌚️ {HM}"
        logger.info(bio)
        await event.edit('''ساعت در بیوگرافی با موفقیت ست شد ☑️
نویسنده  @MHMOFFICIAL''')
        try:
            await client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await client.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)















from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User



logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

@client.on(events.NewMessage(pattern='.count'))  
async def stats(event: NewMessage.Event) -> None:  # pylint: disable = R0912, R0914, R0915
    """Command to get stats about the account"""
    waiting_message = await event.edit('`Collecting stats, Wait Master`')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog, limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1

            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1

        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1

        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time

    full_name = inline_mention(await event.client.get_me())
    response = f'🔸 **مشخصات برای {full_name}** \n\n'
    response += f'**چت های شخصی:** {private_chats} \n'
    response += f'   • `یوزر ها: {private_chats - bots}` \n'
    response += f'   • `ربات ها: {bots}` \n'
    response += f'**گروه ها:** {groups} \n'
    response += f'**چنل ها:** {broadcast_channels} \n'
    response += f'**ادمین شده در گروه ها:** {admin_in_groups} \n'
    response += f'   • `سازنده گروه: {creator_in_groups}` \n'
    response += f'   • `دسترسی به ادمین: {admin_in_groups - creator_in_groups}` \n'
    response += f'**ادمینیت برای چنل:** {admin_in_broadcast_channels} \n'
    response += f'   • `چنل های ساخته شده توسط شما: {creator_in_channels}` \n'
    response += f'   • `چنل هایی که دسترسی ادمین دارید: {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'**پیام های خوانده نشده:** {unread} \n'
    response += f'**مارک های خانده نشده:** {unread_mentions} \n\n'
    response += f'__It Took:__ {stop_time:.02f}s \n'

    await event.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name



from collections import deque


@client.on(events.NewMessage(pattern=r"\.earth", outgoing=True))
async def earth(event):
	if event.fwd_from:
		return
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@client.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@client.on(events.NewMessage(pattern=r"\.clan", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@client.on(events.NewMessage(pattern=r".jio"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 19)

   # input_str = event.pattern_match.group(1)

   # if input_str == "jio":

    await event.edit("jio")

    animation_chars = [
        
            "Connecting To JIO Network 📡 ....",
            "█ ▇ ▆ ▅ ▄ ▂ ▁",
            "▒ ▇ ▆ ▅ ▄ ▂ ▁",
            "▒ ▒ ▆ ▅ ▄ ▂ ▁",
            "▒ ▒ ▒ ▅ ▄ ▂ ▁",    
            "▒ ▒ ▒ ▒ ▄ ▂ ▁",
            "▒ ▒ ▒ ▒ ▒ ▂ ▁",
            "▒ ▒ ▒ ▒ ▒ ▒ ▁",
            "▒ ▒ ▒ ▒ ▒ ▒ ▒",
            "*Optimising Network....*",
            "▒ ▒ ▒ ▒ ▒ ▒ ▒",
            "▁ ▒ ▒ ▒ ▒ ▒ ▒",           
            "▁ ▂ ▒ ▒ ▒ ▒ ▒",
            "▁ ▂ ▄ ▒ ▒ ▒ ▒",
            "▁ ▂ ▄ ▅ ▒ ▒ ▒",
            "▁ ▂ ▄ ▅ ▆ ▒ ▒",
            "▁ ▂ ▄ ▅ ▆ ▇ ▒",
            "▁ ▂ ▄ ▅ ▆ ▇ █",
            "JIO Network Connected and Boosted...."

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 19])




@client.on(events.NewMessage(pattern="(.*)"))
async def think(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "think":
        await event.edit(input_str)
        animation_chars = [
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING... 🤔",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])




from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.tl import functions


@client.on(events.NewMessage(pattern="clone ?(.*)"))
async def Clone(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(user_id,Download_path)
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their names
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
      last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    # giving myself credits cause y not
    user_bio = replied_user.about
    if user_id == 906582956:
        await event.edit("شرمنده سازندمو نمیتونی کلون کنید ✔")
        await asyncio.sleep(3)
        return
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    await client(functions.account.UpdateProfileRequest(
        first_name=first_name
    ))
    await client(functions.account.UpdateProfileRequest(
        last_name=last_name
    ))
    await client(functions.account.UpdateProfileRequest(
        about=user_bio
    ))
    n = 1
    pfile = await client.upload_file(profile_pic)  # pylint:disable=E060      
    await client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
        pfile
    ))
    #message_id_to_reply = event.message.reply_to_msg_id
    #if not message_id_to_reply:
    #    message_id_to_reply = event.message.id
    #await client.send_message(
    #  event.chat_id,
    #  "Hey ? Whats Up !",
    #  reply_to=message_id_to_reply,
    #  )
    await event.delete()
    await client.send_message(
      event.chat_id,
      "**پروفایل کاربر مورد نظر با موفقیت کپی‌شد**",
      reply_to=reply_message
      )

async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e





@client.on(events.NewMessage(pattern=r"\.help"))
async def help(event):
    if event.fwd_from:
        return
    await event.edit("⚡️ به راهنمای سلف MHM خوش امدید ⚡️")
    await event.reply(''' دستورات به شرح زیر میباشد :
ورژن شما 1
➖➖➖➖➖➖➖➖➖➖

.clone

جهت کپی مو به موی یک اکانت روی اکانت شما 
یعنی پروفایل ها بایوگرافی و اسم و‌فامیل اون اکانتو دقیقا میزاره رو اکانت شما 
نمونه استفاده:
.clone @MHMsupport

➖➖➖➖➖➖➖➖➖➖

.weather 

جهت گرفتن اب و هوای شهر شما 
نحوه استفاده به طور مثال:
.weather تهران

➖➖➖➖➖➖➖➖➖➖

.say 

جهت نوشتن یک تکست به صورت لایو 
نمونه:

.say سلام این‌ یک تست است

➖➖➖➖➖➖➖➖➖➖

.think

این یک دستور فان هست و میگوید من‌دارم‌ فکر میکنم

➖➖➖➖➖➖➖➖➖➖

.yta

برای دانلود کردن یک فیلم از یوتوب به صورت mp3
در جلوی .yta لینک خود را قرار دهید 
⚠️توجه این عملیات ممکن است طول بکشد⚠️
اگه داخل ترموکس ران کردید از حجم اینترنت شما استفاده میشه

➖➖➖➖➖➖➖➖➖➖

.ytv 

برای دانلود کردن یه دیدیو از یوتوب با فرمت ویدیو .mp4 
جولوی .ytv لینک خود را قرار دهید
⚠️توجه این عملیات ممکن است طول بکشد⚠️
اگه داخل ترموکس ران کردید از حجم اینترنت شما استفاده میشه

➖➖➖➖➖➖➖➖➖➖

.voice 
برای تبدیل یک تکست به صدا 
نحوه استفاده بدین شکل است که روی یک پیام ریپلی میکنید و دستور .voice رو روش میزنید و جولوی .voice کد کشور رو هم قرار میدید 
متاسفانه زبان فارسی پشتیبانی نمیشه
کد چند کشور :
en به معنای انگلیسی
ar به معنای عربی
de به معنای المانی

نحوه استفاده اول ریپلی بزنید و بعد:
.voice en

➖➖➖➖➖➖➖➖➖➖

.tagall

جهت تگ کردن افراد یک گروه

➖➖➖➖➖➖➖➖➖➖

.tagadmin

جهت تگ کردن ادمین های یک گروه

➖➖➖➖➖➖➖➖➖➖

.info

جهت گرفتن مشخصات اکانت یک‌ شخص 
اگه داخل پیویش بنویسید مشخصات اکانتشو میده 
اگه جولوی .voice یک ایدی و یا یوزر ایدی بزارید مشخصات اون یوزرو به شما میده 
مثال:
.info @MHMsupport

➖➖➖➖➖➖➖➖➖➖

.count 

جهت گرفتن‌ یک مشخصات کلی از اکانت شما

➖➖➖➖➖➖➖➖➖➖

.pname
جهت عوض کردن اسم شما در تلگرام
مثال :

.pname محمد

➖➖➖➖➖➖➖➖➖➖

.pbio 

جهت تنظیم یک بایوگرافی جدید مثال :

.pbio این یک بیوگرافی جدید است

➖➖➖➖➖➖➖➖➖➖

.ppic 

جهت ثبت کردن پروفایل جدید 
نحوه استفاده بدین شکل است که .ppic را بنویسید و روی یک عکس ریپلی کنی

➖➖➖➖➖➖➖➖➖➖

.bioclock 

جهت تنظیم ساعت در بایوگرافی 

➖➖➖➖➖➖➖➖➖➖

.jio 

یک دستور فان و مدام در حال ادیت

➖➖➖➖➖➖➖➖➖➖

.earth 

جهت نمایش دادن چرخش کره زمین 

➖➖➖➖➖➖➖➖➖➖

.moon

جهت نمایش دادن چرخش ماه

➖➖➖➖➖➖➖➖➖➖

.clan

جهت نمایش دادن چرخش ساعت

➖➖➖➖➖➖➖➖➖➖

.react happy
.react thinking
.react waving
.react wtf
.react love
.react confused 
.react ded
.react sad 
.react dog
.react 

این دستورات شمارو به حالت های مختلف نشون‌میده و فان هست
توجه کنید که ممکن است هر بار یک ری اکشن جدید رو بده حتی اگه تکراری باشه دستور چون چند ری اکشن داخلشون ثبت شده

➖➖➖➖➖➖➖➖➖➖

.windows
.linux
.stock
.os

جهت نمایش دادن مشخصات سیستم شما 
بهتر هست از دستوری استفاده کنید که روش باتو ران کردید اگه روی ترموکس ران کردید باید بدید .linux



ورژن سلف 1
نوشته شده توسط @CyberProgram 
چنل : @MHMOFFICIAL''')

       
asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
app.run()
