from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

pmtags = []

feri = 'BABeirG8XZbo79Qu4oOQVlv03JnBsEKUHi31hiVIKFjbCvWpViec-7FUAZUAcrCDbi_7yVmR7HwzkaV957zCsthd0QfWusGwSKLQxd06jwSndBgQwFBd-vKeawz-shGefbp8Rba-9x0qcXS6AQu2DI7BK9VhNqWvW-A0p8GvDQMXOvLRMqnkTyENnJW4ruAVHbGISmFvGZQSXg0FTWReNLG7XSvlXjqXTr9HoiOTVLTky7nbA5X9QqAgF-kLjpMCTOdDNCbxIvnATEKxXAmBvwEP14GghRO27Auwfg-l6O6BKAlRbFcGQ1yZerm0XwIGLHXd2FkxYMNjBiszae9qOgKMffQeHQA'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

men = True

edc = []
edc2 = []
edc3 = []
edc4 = []
edc5 = []

me = [2113150493]

@app.on_message (filters.user(me) & (filters.text | filters.sticker) & (filters.group | filters.private))
def myself(c, m):
    chatid = m.chat.id
    chatti = m.chat.title
    msgid = m.message_id
    fname = m.from_user.first_name
    global banner
    global group
    global pmping
    global men
    global mtxt
    global msp
    global asp
    global adsp
    global bn
    global unbn
    global edc,edc2,edc3,edc4,edc5
    global eds,eds2,eds3,eds4,eds5
    global edp,edp2,edp3,edp4,edp5
    if m.text == "setping" or m.text == "Setping":
        pmping = m.reply_to_message.text
        app.edit_message_text(m.chat.id, msgid, "**『Ping message set✅』**")
    elif m.text == "ping" or m.text == "Ping":
        app.edit_message_text(chatid, msgid, f"{pmping}", parse_mode="HTML")
    elif m.text == "delping" or m.text == "Delping":
        pmping = ""
        app.edit_message_text(chatid, msgid, "**『Ping message deleted🗑✔』**")

    elif m.text == "Stats" or m.text == "امار ها":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={target.id}&json=true").json()
        if not stats:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={target.id})")
                return
        tedadBazia = stats["gamesPlayed"]
        tedadBord = stats["won"]["total"]
        darsadBord = stats["won"]["percent"]
        tedadBakht = stats["lost"]["total"]
        darsadBakht = stats["lost"]["percent"]
        app.edit_message_text(chatid, msgid, f"""**•User information ➥ [{target.first_name}](tg://user?id={target.id})
•Games ➥ {tedadBazia}
•win ➥ {tedadBord} ⊰%{darsadBord}⊱ 
•Lost ➥ {tedadBakht} ⊰%{darsadBakht}⊱**""")

    elif m.text == "Kills" or m.text == "قتل ها":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={target.id}&json=true").json()
        if not s:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={target.id})")
                return
        text = f'''**•User information ➥[{target.first_name}](tg://user?id={target.id})
•kills list:**
'''
        i = 999994
        for user in s:
            text += f'**{i+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            text
            i += 1
            text = text.replace('999995','•1 ➥')
            text = text.replace('999996','•2 ➥')
            text = text.replace('999997','•3 ➥')
            text = text.replace('999998','•4 ➥')
            text = text.replace('999999','•5 ➥')
        app.edit_message_text(chatid, msgid, text) 

    elif m.text == "Killedby" or m.text == "قاتل ها":
        if m.reply_to_message:
            targ = m.reply_to_message.from_user
        else:
            targ = m.from_user
        t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={targ.id}&json=true").json()
        if not t:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={targ.id})")
                return
        tixt = f'''**•User information ➥ [{targ.first_name}](tg://user?id={targ.id})
•killedby list:**
'''
        o = 999994
        for user in t:
            tixt += f'**{o+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            o += 1
            tixt = tixt.replace('999995','•1 ➥')
            tixt = tixt.replace('999996','•2 ➥')
            tixt = tixt.replace('999997','•3 ➥')
            tixt = tixt.replace('999998','•4 ➥')
            tixt = tixt.replace('999999','•5 ➥')
        app.edit_message_text(chatid, msgid, tixt)

    elif m.text == "Userid" or m.text == "userid":
        if m.reply_to_message:
            tar = m.reply_to_message.from_user
        else:
            tar = m.from_user
        app.edit_message_text(chatid, msgid, f'''**•User ID [{tar.first_name}](tg://user?id={tar.id}) Found**
**•User ID ➥** `{tar.id}`''')

    if "Userid" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**•User ID [{ids.first_name}](tg://user?id={ids.id}) Found**
**•User ID ➥** `{ids.id}`''')
    if "userid" in m.text:
      users = m.text.split()[2]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**•User ID [{ids.first_name}](tg://user?id={ids.id}) Found**
**•User ID ➥** `{ids.id}`''')

    if "Userse" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**『 User [{ids.first_name}](tg://user?id={ids.id}) Found 』**")
    if "userse" in m.text:
      users = m.text.split()[3]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**『 User [{ids.first_name}](tg://user?id={ids.id}) Found  』**")

    if m.text == "groupid" or m.text == "Groupid":
      app.edit_message_text(chatid, msgid, f'''**•Group ID ➥ {chatti} Found**
**•Group ID ➥** `{chatid}`''')

    if "Stats" in m.text:
      userss = m.text.split()[1]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**•User information ➥ [{idss.first_name}](tg://user?id={idss.id})
•Games ➥ {tedadBazia}
•win ➥ {tedadBord} (%{darsadBord}) 
•Lost ➥ {tedadBakht} (%{darsadBakht})**""")
    if "Games" in m.text:
      userss = m.text.split()[2]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[『 No Stats 』](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**•User information ➥[{idss.first_name}](tg://user?id={idss.id})
•Games ➥ {tedadBazia}
•win ➥ {tedadBord} (%{darsadBord}) 
•Lost ➥ {tedadBakht} (%{darsadBakht})**""")

    elif "قتل ها" in m.text:
      usersss = m.text.split()[2]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[『 No Stats  』](tg://user?id={idsss.id})")
                return
      text = f'''**•User information ➥ [{idsss.first_name}](tg://user?id={idsss.id})
•List Kills:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            text
            i += 1
            text = text.replace('999995','•1 ➥')
            text = text.replace('999996','•2 ➥')
            text = text.replace('999997','•3 ➥')
            text = text.replace('999998','•4 ➥')
            text = text.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, text)
    elif "Kills" in m.text:
      usersss = m.text.split()[1]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[『 No Stats  』](tg://user?id={idsss.id})")
                return
      text = f'''**•User information ➥[{idsss.first_name}](tg://user?id={idsss.id})
•List Kills:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            text
            i += 1
            text = text.replace('999995','•1 ➥')
            text = text.replace('999996','•2 ➥')
            text = text.replace('999997','•3 ➥')
            text = text.replace('999998','•4 ➥')
            text = text.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, text)

    elif "Killedby" in m.text:
      userssss = m.text.split()[1]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[『 No Stats 』](tg://user?id={idssss.id})")
                return
      tixt = f'''**•User information ➥[{idssss.first_name}](tg://user?id={idssss.id})
•List killedby:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            o += 1
            tixt = tixt.replace('999995','•1 ➥')
            tixt = tixt.replace('999996','•2 ➥')
            tixt = tixt.replace('999997','•3 ➥')
            tixt = tixt.replace('999998','•4 ➥')
            tixt = tixt.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, tixt)
    elif "قاتل ها" in m.text:
      userssss = m.text.split()[2]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[『 No Stats 』](tg://user?id={idssss.id})")
                return
      tixt = f'''**•User information [{idssss.first_name}](tg://user?id={idssss.id})
•List killedby:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            o += 1
            tixt = tixt.replace('999995','•1 ➥')
            tixt = tixt.replace('999996','•2 ➥')
            tixt = tixt.replace('999997','•3 ➥')
            tixt = tixt.replace('999998','•4 ➥')
            tixt = tixt.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, tixt)

    if m.text == "Setbanner" or m.text == "تنظیم بنر":
      banner = m.reply_to_message.text
      app.edit_message_text(m.chat.id, msgid, "**『 Banner set✅ 』**")
    elif m.text == "Getbanner" or m.text == "دریافت بنر":
      app.edit_message_text(m.chat.id, msgid, f"""**•the last banner set**
**•Banner ➥** `{banner}`""")
    elif "Startatk" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Adjusting banner upload speed...  』**")
        adsp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 Banner upload speed set ✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Receiving user information... 』**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Information required by users was received 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start✅  』**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Stop🛑 』**")
    elif "startatk" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Adjusting banner upload speed...  』**")
        adsp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 Banner upload speed set ✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Receiving user information... ! 』**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Information required by users was received 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start✅ 』**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake  』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Stop🛑 』**")

    elif "Adduser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group...  』**")
        agp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Group✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed... 』**")
        asp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get users...  』**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Get users✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start Add...  』**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**『 User Add✅ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**『 Try another 7 minutes⛔ 』**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**『 Stop Add🛑 』**")
    elif "adduser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group... 』**")
        agp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Group✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed... 』**")
        asp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get users... 』**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Get users✔』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start Add... 』**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**『 User Add✅ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**『 Try another 7 minutes⛔ 』**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**『 Stop Add🛑 』**")

    if "Tagg" in m.text:
        msp = m.text.split()[1]
        app.delete_messages(chatid, m.message_id)
        try:       
            men = True
            chat_members = app.get_chat_members(chatid)
            for i in chat_members:
                if men:
                    if i.user.first_name:
                        if i.user.id == me:
                            continue
                        name = i.user.first_name
                        userid = i.user.id
                        title = m.chat.title
                        mention = f"[{name}](tg://user?id={userid})"
                        s = app.send_message(chatid, mtxt.format(mention=mention,title=title,userid=userid,name=name))
                        sleep(int(msp))
                        pmtags.append(s.message_id)
                    else:
                        print("Delete Account!")
                        pmtags.clear()
        except pyrogram.errors.exceptions.flood_420.FloodWait:
            app.send_message(m.chat.id, "**『 Try another 7 minutes⛔ 』**")
    if m.text == "Settg" or m.text == "Settg":
      mtxt = f"{m.reply_to_message.text}"
      app.edit_message_text(m.chat.id, msgid, "**『 set✅ 』**")
    elif m.text == "Gettg" or m.text == "Gettg":
      app.edit_message_text(m.chat.id, msgid, f"""**•Text tag **
**•Text tag:** `{mtxt}`""")
    elif m.text == "Stop" or m.text == "Stop":
        men = False
        app.delete_messages(chatid, m.message_id)
    elif m.text == "Del" or m.text == "Del":
        men = False
        app.delete_messages(chatid, m.message_id)
        app.delete_messages(chatid, pmtags)

    if "Listuser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group... 』**")
        gp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 Set group✅ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get Users...  』**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**『 ✅ 』**")
        gmtext = "**『 List Group♻️ 』**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)
    if "listuser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group... 』**")
        gp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**『 Set group✅ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get Users...  』**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**『 ✅ 』**")
        gmtext = "**『 List Group♻️ 』**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)

    if m.text == "ban" or m.text == "Ban":
        app.ban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**『 [User](tg://user?id={m.reply_to_message.from_user.id}) Ban📛 』**")
    if m.text == "unban" or m.text == "Unban":
        app.unban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**『 [User](tg://user?id={m.reply_to_message.from_user.id}) Un ban ✅ 』**")
        
    if m.text.split()[0] == "setedit1":
        edc.clear()
        edc.append(m.text.split()[1])
        eds = m.text.split()[2]
        edp = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc:
        edi = ""
        for i in edp.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds))

    if m.text.split()[0] == "setedit2":
        edc2.clear()
        edc2.append(m.text.split()[1])
        eds2 = m.text.split()[2]
        edp2 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc2:
        edi = ""
        for i in edp2.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds2))

    if m.text.split()[0] == "setedit3":
        edc3.clear()
        edc3.append(m.text.split()[1])
        eds3 = m.text.split()[2]
        edp3 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc3:
        edi = ""
        for i in edp3.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds3))

    if m.text.split()[0] == "setedit4":
        edc4.clear()
        edc4.append(m.text.split()[1])
        eds4 = m.text.split()[2]
        edp4 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc4:
        edi = ""
        for i in edp4.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds4))

    if m.text.split()[0] == "setedit5":
        edc5.clear()
        edc5.append(m.text.split()[1])
        eds5 = m.text.split()[2]
        edp5 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc5:
        edi = ""
        for i in edp5.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds5))

app.run()
