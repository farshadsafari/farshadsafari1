from pyrogram import Client, filters
import random
from time import sleep
feri = 'BAAK-xvePWLi5TaQwYKSHX249UsL1ptjmQke25WiSk5SXJr18ANYsNxQ38ZndswDUovazfrgjmjHpvEmIrqdpmx2xjqU-sMMYs4LJ1Rl2Tb4Fwb8I62v_lPzjjSqTvCulshrMxkQQmhfccGMks-eyqGtWMWsgE9tL4GhitgIGdXtcVwdUZz9oEcy-u8CE2cYcrnZCVtmHOmvGD_bh8P1t8atYVstIKbo7B69FbFsTFRQYCXyiNa95mDcroLCAHOAS-wsUPiwMMM89VAI-cGwNBAa3uvA4iHzrd9F6Tp6xnCd8IYqE2XjKZNaF2VOvBpcm5PgbI_OQ7sAaf_tJjJ9uWWUAAAAATuwAm0A'
app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

safe = []

with app:
    me = app.get_me().id

helpmsg = """**If you do not want to block the message, put the message in PV
/n safeyou /n
If someone was safe and you wanted to get out of safe
/n dsafeyou /n
Click on his message

People who are not safe will be automatically blocked if they send a sticker, link or ID, and the message sent in PV will be saved in Siomessage by mentioning the sender.**"""

@app.on_message(filters.regex("my helpp") & filters.private)
def help_msg(client,message):
    message.reply_text(helpmsg)

@app.on_message(filters.text & filters.private)
def anti_attack(c, m):
    if m.text == 'safeyou':
        user = m.reply_to_message.from_user
        safe.append(user.id)
        app.send_message(m.chat.id,f"{user.mention}**Added to safe list✔**")

    if m.text == 'dsafeyou':
        user = m.reply_to_message.from_user
        safe.remove(user.id)
        app.send_message(m.chat.id,f"{user.mention}**Removed from safe list🗑✔**")

    if "t.me" in m.text and m.from_user.id not in safe:
        app.send_message(me, f"[A link was received from him and was blocked](tg://user?id={m.from_user.id})")
        app.send_message(me, "**Link sent:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

    if "@" in m.text and m.from_user.id not in safe:
        app.send_message(me, f"[An ID was received from him and it was blocked](tg://user?id={m.from_user.id})")
        app.send_message(me, "**Posted ID:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

@app.on_message(filters.sticker & filters.private)
def st_attack(c,m):
    if m.chat.id not in safe:
        app.send_message(me, f"[A sticker was received from him and it was blocked](tg://user?id={m.from_user.id})")
        app.send_message(me, "**Sticker sent:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

@app.on_message(filters.caption & filters.private)
def cap_attack(c, m):
    if "t.me" in m.caption and m.from_user.id not in safe:
        app.send_message(me, f"[A link was received from him and was blocked](tg://user?id={m.from_user.id})")
        app.send_message(me, "**Link sent:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

    if "@" in m.caption and m.from_user.id not in safe:
        app.send_message(me, f"[An ID was received from him and it was blocked](tg://user?id={m.from_user.id})")
        app.send_message(me, "**Posted ID:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)
app.run()
