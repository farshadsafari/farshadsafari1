from pyrogram import Client, filters
import random
from time import sleep
feri = 'BABeirG8XZbo79Qu4oOQVlv03JnBsEKUHi31hiVIKFjbCvWpViec-7FUAZUAcrCDbi_7yVmR7HwzkaV957zCsthd0QfWusGwSKLQxd06jwSndBgQwFBd-vKeawz-shGefbp8Rba-9x0qcXS6AQu2DI7BK9VhNqWvW-A0p8GvDQMXOvLRMqnkTyENnJW4ruAVHbGISmFvGZQSXg0FTWReNLG7XSvlXjqXTr9HoiOTVLTky7nbA5X9QqAgF-kLjpMCTOdDNCbxIvnATEKxXAmBvwEP14GghRO27Auwfg-l6O6BKAlRbFcGQ1yZerm0XwIGLHXd2FkxYMNjBiszae9qOgKMffQeHQA'
app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

safe = []

with app:
    me = app.get_me().id

helpmsg = """**حال نداشتم هلپ بنویسم سعی کنین بفهمین
کسی که میخواین درصورت پیام دادن بلاک نشه رو پیامش تو پی وی بزنید 
safe
اگر شخصی سیف بود و خواستید از سیف خارج بشه
dsafe
بزنید روی پیامش

افرادی که سیف نیستند اگر استیکر یا لینک یا آیدی بفرستند اتومات بلاک میشوند و مسیج ارسالی در پی وی با ذکر شخص فرستنده در سیومسیج سیو میشه**"""

@app.on_message(filters.regex("my helpp") & filters.private)
def help_msg(client,message):
    message.reply_text(helpmsg)

@app.on_message(filters.text & filters.private)
def anti_attack(c, m):
    if m.text == 'safeyou':
        user = m.reply_to_message.from_user
        safe.append(user.id)
        app.send_message(m.chat.id,f"{user.mention}**به سیف لیست اضافه شد**")

    if m.text == 'dsafeyou':
        user = m.reply_to_message.from_user
        safe.remove(user.id)
        app.send_message(m.chat.id,f"{user.mention}**از سیف لیست حذف شد**")

    if "t.me" in m.text and m.from_user.id not in safe:
        app.send_message(me, f"[یک لینک دریافت شد از ایشون و بلاک شد](tg://user?id={m.from_user.id})")
        app.send_message(me, "**لینک ارسال شده:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

    if "@" in m.text and m.from_user.id not in safe:
        app.send_message(me, f"[یک آیدی دریافت شد از ایشون و بلاک شد](tg://user?id={m.from_user.id})")
        app.send_message(me, "**آیدی ارسال شده:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

@app.on_message(filters.sticker & filters.private)
def st_attack(c,m):
    if m.chat.id not in safe:
        app.send_message(me, f"[یک استیکر دریافت شد از ایشون و بلاک شد](tg://user?id={m.from_user.id})")
        app.send_message(me, "**استیکر ارسال شده:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

@app.on_message(filters.caption & filters.private)
def cap_attack(c, m):
    if "t.me" in m.caption and m.from_user.id not in safe:
        app.send_message(me, f"[یک لینک دریافت شد از ایشون و بلاک شد](tg://user?id={m.from_user.id})")
        app.send_message(me, "**لینک ارسال شده:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)

    if "@" in m.caption and m.from_user.id not in safe:
        app.send_message(me, f"[یک آیدی دریافت شد از ایشون و بلاک شد](tg://user?id={m.from_user.id})")
        app.send_message(me, "**آیدی ارسال شده:**")
        app.forward_messages(me, m.chat.id, m.message_id)
        app.block_user(user_id=m.chat.id)
        app.delete_messages(m.chat.id, m.message_id)
app.run()
