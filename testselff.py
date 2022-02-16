
from pyrogram import Client, Filters as filters
from requests import get
import pyrogram
import json
from time import sleep

pmtags = []

feri = 'BAAK-xvePWLi5TaQwYKSHX249UsL1ptjmQke25WiSk5SXJr18ANYsNxQ38ZndswDUovazfrgjmjHpvEmIrqdpmx2xjqU-sMMYs4LJ1Rl2Tb4Fwb8I62v_lPzjjSqTvCulshrMxkQQmhfccGMks-eyqGtWMWsgE9tL4GhitgIGdXtcVwdUZz9oEcy-u8CE2cYcrnZCVtmHOmvGD_bh8P1t8atYVstIKbo7B69FbFsTFRQYCXyiNa95mDcroLCAHOAS-wsUPiwMMM89VAI-cGwNBAa3uvA4iHzrd9F6Tp6xnCd8IYqE2XjKZNaF2VOvBpcm5PgbI_OQ7sAaf_tJjJ9uWWUAAAAATuwAm0A'
app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

men = True

edc = []
edc2 = []
edc3 = []
edc4 = []
edc5 = []

me = [5296357997]

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
    if m.text == "setpingtext" or m.text == "تنظیم پیام پینگ":
        pmping = m.reply_to_message.text
        app.edit_message_text(m.chat.id, msgid, "**『 پیام پینگ تنظیم شد ! 』**")
    elif m.text == "ping" or m.text == "پینگ":
        app.edit_message_text(chatid, msgid, f"{pmping}", parse_mode="HTML")
    elif m.text == "deletepingtext" or m.text == "حذف پیام پینگ":
        pmping = ""
        app.edit_message_text(chatid, msgid, "**『 پیام پینگ پاک شد ! 』**")

    elif m.text == "stats" or m.text == "بازی ها":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={target.id}&json=true").json()
        if not stats:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={target.id})")
                return
        tedadBazia = stats["gamesPlayed"]
        tedadBord = stats["won"]["total"]
        darsadBord = stats["won"]["percent"]
        tedadBakht = stats["lost"]["total"]
        darsadBakht = stats["lost"]["percent"]
        app.edit_message_text(chatid, msgid, f"""**┓ اطلاعات کاربر: [{target.first_name}](tg://user?id={target.id})
┫ بازی های انجام شده: {tedadBazia}
┫ برد ها: {tedadBord} (%{darsadBord}) 
┛ باخت ها: {tedadBakht} (%{darsadBakht})**""")

    elif m.text == "kills" or m.text == "قتل ها":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={target.id}&json=true").json()
        if not s:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={target.id})")
                return
        text = f'''**┓ اطلاعات کاربر [{target.first_name}](tg://user?id={target.id})
┫ کسانی که شما کشته اید:**
'''
        i = 999994
        for user in s:
            text += f'**{i+1} {user["name"]} (`{user["times"]}`)**\n'
            text
            i += 1
            text = text.replace('999995','┫ اول:')
            text = text.replace('999996','┫ دوم:')
            text = text.replace('999997','┫ سوم:')
            text = text.replace('999998','┫ چهارم:')
            text = text.replace('999999','┛ پنجم:')
        app.edit_message_text(chatid, msgid, text)

    elif m.text == "killedby" or m.text == "قاتل ها":
        if m.reply_to_message:
            targ = m.reply_to_message.from_user
        else:
            targ = m.from_user
        t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={targ.id}&json=true").json()
        if not t:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={targ.id})")
                return
        tixt = f'''**┓ اطلاعات کاربر [{targ.first_name}](tg://user?id={targ.id})
┫ کسانی که شما را کشته اند:**
'''
        o = 999994
        for user in t:
            tixt += f'**{o+1} {user["name"]} (`{user["times"]}`)**\n'
            o += 1
            tixt = tixt.replace('999995','┫ اول:')
            tixt = tixt.replace('999996','┫ دوم:')
            tixt = tixt.replace('999997','┫ سوم:')
            tixt = tixt.replace('999998','┫ چهارم:')
            tixt = tixt.replace('999999','┛ پنجم:')
        app.edit_message_text(chatid, msgid, tixt)

    elif m.text == "userid" or m.text == "شناسه کاربر":
        if m.reply_to_message:
            tar = m.reply_to_message.from_user
        else:
            tar = m.from_user
        app.edit_message_text(chatid, msgid, f'''**┓** **شناسه کاربر [{tar.first_name}](tg://user?id={tar.id}) پیدا شد**
**┛ شناسه کاربر:** `{tar.id}`''')

    if "userid" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**┓** **شناسه کاربر [{ids.first_name}](tg://user?id={ids.id}) پیدا شد**
**┛ شناسه کاربر:** `{ids.id}`''')
    if "شناسه کاربر" in m.text:
      users = m.text.split()[2]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**┓** **شناسه کاربر [{ids.first_name}](tg://user?id={ids.id}) پیدا شد**
**┛ شناسه کاربر:** `{ids.id}`''')

    if "finduser" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**『 کاربر [{ids.first_name}](tg://user?id={ids.id}) پیدا شد ! 』**")
    if "پیدا کردن کاربر" in m.text:
      users = m.text.split()[3]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**『 کاربر [{ids.first_name}](tg://user?id={ids.id}) پیدا شد ! 』**")

    if m.text == "groupid" or m.text == "شناسه گروه":
      app.edit_message_text(chatid, msgid, f'''**┓** **شناسه گروه {chatti} پیدا شد**
**┛ شناسه گروه:** `{chatid}`''')

    if "stats" in m.text:
      userss = m.text.split()[1]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**┓ اطلاعات کاربر: [{idss.first_name}](tg://user?id={idss.id})
┫ بازی های انجام شده: {tedadBazia}
┫ برد ها: {tedadBord} (%{darsadBord}) 
┛ باخت ها: {tedadBakht} (%{darsadBakht})**""")
    if "بازی ها" in m.text:
      userss = m.text.split()[2]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**┓ اطلاعات کاربر: [{idss.first_name}](tg://user?id={idss.id})
┫ بازی های انجام شده: {tedadBazia}
┫ برد ها: {tedadBord} (%{darsadBord}) 
┛ باخت ها: {tedadBakht} (%{darsadBakht})**""")

    elif "قتل ها" in m.text:
      usersss = m.text.split()[2]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={idsss.id})")
                return
      text = f'''**┓ اطلاعات کاربر [{idsss.first_name}](tg://user?id={idsss.id})
┫ کسانی که شما کشته اید:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} (`{user["times"]}`)**\n'
            text
            i += 1
            text = text.replace('999995','┫ اول:')
            text = text.replace('999996','┫ دوم:')
            text = text.replace('999997','┫ سوم:')
            text = text.replace('999998','┫ چهارم:')
            text = text.replace('999999','┛ پنجم:')
      app.edit_message_text(chatid, msgid, text)
    elif "kills" in m.text:
      usersss = m.text.split()[1]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={idsss.id})")
                return
      text = f'''**┓ اطلاعات کاربر [{idsss.first_name}](tg://user?id={idsss.id})
┫ کسانی که شما کشته اید:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} (`{user["times"]}`)**\n'
            text
            i += 1
            text = text.replace('999995','┫ اول:')
            text = text.replace('999996','┫ دوم:')
            text = text.replace('999997','┫ سوم:')
            text = text.replace('999998','┫ چهارم:')
            text = text.replace('999999','┛ پنجم:')
      app.edit_message_text(chatid, msgid, text)

    elif "killedby" in m.text:
      userssss = m.text.split()[1]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={idssss.id})")
                return
      tixt = f'''**┓ اطلاعات کاربر [{idssss.first_name}](tg://user?id={idssss.id})
┫ کسانی که شما را کشته اند:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} (`{user["times"]}`)**\n'
            o += 1
            tixt = tixt.replace('999995','┫ اول:')
            tixt = tixt.replace('999996','┫ دوم:')
            tixt = tixt.replace('999997','┫ سوم:')
            tixt = tixt.replace('999998','┫ چهارم:')
            tixt = tixt.replace('999999','┛ پنجم:')
      app.edit_message_text(chatid, msgid, tixt)
    elif "قاتل ها" in m.text:
      userssss = m.text.split()[2]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[『 تا حالا هیچ بازی ای انجام نداده ! 』](tg://user?id={idssss.id})")
                return
      tixt = f'''**┓ اطلاعات کاربر [{idssss.first_name}](tg://user?id={idssss.id})
┫ کسانی که شما را کشته اند:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} (`{user["times"]}`)**\n'
            o += 1
            tixt = tixt.replace('999995','┫ اول:')
            tixt = tixt.replace('999996','┫ دوم:')
            tixt = tixt.replace('999997','┫ سوم:')
            tixt = tixt.replace('999998','┫ چهارم:')
            tixt = tixt.replace('999999','┛ پنجم:')
      app.edit_message_text(chatid, msgid, tixt)

    if m.text == "setbanner" or m.text == "تنظیم بنر":
      banner = m.reply_to_message.text
      app.edit_message_text(m.chat.id, msgid, "**『 بنر تنظیم شد ! 』**")
    elif m.text == "getbanner" or m.text == "دریافت بنر":
      app.edit_message_text(m.chat.id, msgid, f"""**┓ آخرین بنر تنظیم شده اینگونه است**
**┛ بنر:** `{banner}`""")
    elif "sendbanner" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم سرعت ارسال بنر... ! 』**")
        adsp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 سرعت ارسال بنر تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال دریافت اطلاعات کاربران... ! 』**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 اطلاعات مورد نیاز کاربران دریافت شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 شروع ارسال بنر ! 』**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 پایان ارسال بنر ! 』**")
    elif "ارسال بنر" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم سرعت ارسال بنر... ! 』**")
        adsp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 سرعت ارسال بنر تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال دریافت اطلاعات کاربران... ! 』**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 اطلاعات مورد نیاز کاربران دریافت شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 شروع ارسال بنر ! 』**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 پایان ارسال بنر ! 』**")

    elif "addusers" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم گروه افزودن کاربران... ! 』**")
        agp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 گروه افزودن کاربران تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم سرعت افزودن کاربران... ! 』**")
        asp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 سرعت افزودن کاربران تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال دریافت اطلاعات کاربران... ! 』**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 اطلاعات مورد نیاز کاربران دریافت شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 شروع افزودن... ! 』**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**『 افزوده شد ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**『 تنظیمات حساب کاربری این کاربر مانع افزودن آن به گروه میشود ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**『 برای افزودن این کاربر محدودیتی وجود دارد ! 』**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**『 برای افزودن این کاربر محدودیتی وجود دارد ! 』**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**『 افزودن به دلیل بر خورد با محدودیت تلگرام متوقف شد بعد از هفت دقیقه میتوانم ادامه دهم ! 』**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**『 پایان افزودن ! 』**")
    elif "افزودن کاربران" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم گروه افزودن کاربران... ! 』**")
        agp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 گروه افزودن کاربران تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم سرعت افزودن کاربران... ! 』**")
        asp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**『 سرعت افزودن کاربران تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال دریافت اطلاعات کاربران... ! 』**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 اطلاعات مورد نیاز کاربران دریافت شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 شروع افزودن... ! 』**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**『 افزوده شد ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 با نام کاربری اشتباه برخورد کردم ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 با تام کاربری اشتباه برخورد کردم ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**『 تنظیمات حساب کاربری این کاربر مانع افزودن آن به گروه میشود ! 』**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**『 برای افزودن این کاربر محدودیتی وجود دارد ! 』**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**『 برای افزودن این کاربر محدودیتی وجود دارد ! 』**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**『 افزودن به دلیل بر خورد با محدودیت تلگرام متوقف شد بعد از هفت دقیقه میتوانم ادامه دهم ! 』**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**『 پایان افزودن ! 』**")

    if "tgs" in m.text:
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
            app.send_message(m.chat.id, "**『 نام بردن به دلیل بر خورد با محدودیت تلگرام متوقف شد بعد از هفت دقیقه میتوانم ادامه دهم ! 』**")
    if m.text == "settgs" or m.text == "ست تگ":
      mtxt = f"{m.reply_to_message.text}"
      app.edit_message_text(m.chat.id, msgid, "**『 پیام نام بردن تنظیم شد ! 』**")
    elif m.text == "gettgs" or m.text == "دریافت پیام نام بردن":
      app.edit_message_text(m.chat.id, msgid, f"""**┓ آخرین پیام نام بردن تنظیم شده اینگونه است**
**┛ پیام نام بردن:** `{mtxt}`""")
    elif m.text == "stoptgs" or m.text == "بسه":
        men = False
        app.delete_messages(chatid, m.message_id)
    elif m.text == "deltgs" or m.text == "پاک":
        men = False
        app.delete_messages(chatid, m.message_id)
        app.delete_messages(chatid, pmtags)

    if "list" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم گروه دریافت اعضا... ! 』**")
        gp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 گروه دریافت اعضا تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال دریافت اطلاعات اعضا گروه... ! 』**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**『 اطلاعات مورد نیاز کامل شد ! 』**")
        gmtext = "**『 لیست اعضا گروه تنظیم شده اینگونه است ! 』**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)
    if "دریافت اعضا گروه" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 در حال تنظیم گروه دریافت اعضا... ! 』**")
        gp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**『 گروه دریافت اعضا تنظیم شد ! 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 در حال دریافت اطلاعات اعضا گروه... ! 』**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**『 اطلاعات مورد نیاز اعضا گروه کامل شد ! 』**")
        gmtext = "**『 لیست اعضا گروه تنظیم شده اینگونه است ! 』**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)

    if m.text == "ban" or m.text == "مسدود":
        app.kick_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**『 [کاربر](tg://user?id={m.reply_to_message.from_user.id}) مسدود شد ! 』**")
    if m.text == "unban" or m.text == "رفع مسدودیت":
        app.unban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**『 [کاربر](tg://user?id={m.reply_to_message.from_user.id}) از لیست مسدود ها حذف شد ! 』**")

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
نویسنده ''')
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
# 500 lines fuckkkkkkkkksssss meeeeeeeee

app.run()
