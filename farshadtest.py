from pyrogram import Client, filters
import random
from time import sleep
feri = 'BACx5OIph6_9dsghZo87y5Vl3juIQ5mTWLg0icvI2VaAU5a-Wv8U_fD7XfLEzDRQNDhLHmfAPQRPbtuwlwVEU9vK21kNFny_yRj6Br4QXNlo4wBhhrp1u6_1EQvYTJMpkbjxwBCA__c2FYV68h9euis7LLxqWvw-_vC72F_ZyQzk-TTsk9Njzf-c1bxqUP2omVPQSOzwEU1x1gC_vE51g3qQcuURB9EusN95GPIi8enADicMByTdSZjJadVl3vdiq0MAFR0qHReYM7nRJEQfqek1hqb24R7VBufVzsatKIWeuFOAqGUEWNdXVVnhkTo_Xe_j0sqTtUSo9C-uaVeRW8EAAAAAATuwAm0A'
tag_stop = {};tags = {};mention = '';tglist = '';speed = 1


app = Client(session_name=feri, api_id=1974143, api_hash='025ac6fb9b7d16993d855de0bc387fee')

@app.on_message(filters.command(['speed'],None))
def spd(client, message):
    global speed
    try:
        speed = int(message.command[1])
        message.reply_text('**Speed  to {} Changed ✅**'.format(speed))
    except Exception:
        message.reply_text('**برای تنظیم سرعت به این شکل عمل کنید\nspeed NUMBER**')
        
@app.on_message(filters.text & filters.user([2113150493,5296357997]) & filters.regex('tag'))
@app.on_message(filters.text & filters.user([2113150493,5296357997]) & filters.regex('deltag'))
@app.on_message(filters.text & filters.regex('stop'))
@app.on_message(filters.text & filters.regex('بسه'))
def tag(client, message):
    global tags, tag_stop
    if message.text.split()[0] == 'tag':
        try:
            text = message.text[5:]
        except:
            text = ''
        tag_stop[message.chat.id] = False
        result2 = app.get_chat_members(message.chat.id, limit=500)
        s = []
        for usr in result2:
            if tag_stop[message.chat.id]:
                break
            if usr.user.id != message.from_user.id and not usr.user.is_bot and usr.user.first_name is not None:
                result = app.send_message(chat_id=message.chat.id,
                                          text=f'[{usr.user.first_name}](tg://user?id={usr.user.id}) {text}')
                s.append(result.message_id)
                sleep(speed)
        try:
            u = tags[message.chat.id]
            u += s
            tags[message.chat.id] = u
        except:
            tags[message.chat.id] = s
    elif message.text.split()[0] == 'deltag':
        try:
            try:
                Ids = tags[message.chat.id]
            except:
                app.send_message(message.chat.id, '**tag pyda nshd !**')
                Ids = message.message_id
            app.send_message(chat_id=message.chat.id,
                                      text="**Ok シ︎**")
            app.delete_messages(chat_id=message.chat.id, message_ids=tags[message.chat.id])
            app.send_message(chat_id=message.chat.id,
                                      text="**tags pak shud✔︎**")
            try:
                tags.pop(message.chat.id)
            except:
                None
        except Exception as e:
            app.send_message(message.chat.id, str(e))
    elif message.text.split()[0] == 'stop':
        tag_stop[message.chat.id] = True
        app.send_message(chat_id=message.chat.id, text='**Ok !**')
    elif message.text.split()[0] == 'بسه':
        tag_stop[message.chat.id] = True
        app.send_message(chat_id=message.chat.id, text='**Ok !**')

wlc_info = {}
wlc_heh = {}

@app.on_message(filters.command("SetWlc","") & filters.user(2113150493))
def setwlc(client,message):
    global wlc_info,wlc_heh
    chat_id = message.chat.id
    if message.reply_to_message:
        wlc_heh[message.chat.id] = True
        wlc_info[chat_id] = message.reply_to_message.text
        message.reply_text("wlc seted.")

@app.on_message(filters.new_chat_members)
def wlc(client,message):
    chat_id = message.chat.id
    try:
        if wlc_heh[message.chat.id]:
            try:
                message.reply_text(wlc_info[chat_id])
            except KeyError:
                return
    except KeyError:
        return
@app.on_message(filters.command("WlcOff","") & filters.user(2113150493))
def wlcof(clientt,message):
    global wlc_heh
    wlc_heh[message.chat.id] = False
  

shekar = r'#ch|#شکار|#شکارم|#شکارچی|#shekar|#shekarchi|لطفا از دستورات ربات استفاده نکنید|#players|فقط یک دقیقه دیگه تا شروع بازی باقی مونده|فقط 30  ثانیه دیگه وقت دارید که وارد بازی شید...|فقط 10  ثانیه دیگه وقت دارید که وارد بازی شید...'
@app.on_message(filters.regex(shekar))
def pin_ch(client, message):
    app.pin_chat_message(message.chat.id,message.message_id)

active = [5296357997,2113150493,205092371,198626752,175844556,742956373]

@app.on_message (filters.text & filters.group & ~filters.edited)
def heln(c, m):
    global nextt
    if "#players" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "/Startchaos",)
    if m.text == "setmtn":
        nextt = m.reply_to_message.text
        app.send_message(m.chat.id,  "**پیام تنظیم شده {setmtn}**")
      
    if "ping" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "**Im Online @farrshad シ︎**", reply_to_message_id=m.message_id)
      
    if "مدت زمان بازی" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "**چه بازی جذابی بود سری جوین شین برای بازی بعدی👻**", reply_to_message_id=m.message_id)
        
    if "• پیام های فرد مورد نظر با موفقیت حذف شدند !" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "delall",reply_to_message_id=m.message_id)         
     
    if "مدت زمان بازی" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "/Startchaos",reply_to_message_id=m.message_id)
    
    if "مدت زمان بازی" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "/Startchaos",)
        
    if "مدت زمان بازی" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "/Startchaos",)
        
app.run()
