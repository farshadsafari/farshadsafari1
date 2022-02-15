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
        message.reply_text('**سرعت تگ به {} تغییر کرد**'.format(speed))
    except Exception:
        message.reply_text('**برای تنظیم سرعت به این شکل عمل کنید\nspeed NUMBER**')

@app.on_message(filters.command('help',None))
def help_me(client,message):
    message.reply_text("""**دستورات تگر سلف\n
برای تنظیم سرعت تگ🔥\n
speed\n
مثالspeed 0
برای صدا کردن💥:\n
tag\n
برای جلوگیری از تگ💦\n
بسه\n
پاکسازی تگ با دستور✅ :\n
DEL\n

پین کردن هشتگ های شکار با سرعت زیاد📌

اسپن متن🔥

دستورات اسپن متن🧑‍💻

بـــرایـــــ پــــاکـــــ کــــردنــــــ اســـــپـــــنــــ مــــتــــنـــــ RESET

بـــــرایـــــ اســـپــــنــــ کـــــردنــــــ 
aspn

بــــرایـــــ ثـــبــــتـــ کــــردنـــــــ مــــتـــنـــــ
sptmin

بــرایــــ جـــلــوگــیـــریـــ از اســــپـــنــــ 
بسه

برای خرید ربات ب پیوی
@mahdi01m
ایشون بروید 

ساخته شده توسط #👀mahdi👀**""")

@app.on_message(filters.text & filters.regex('tag'))
@app.on_message(filters.text & filters.regex('DEL'))
@app.on_message(filters.text & filters.regex('بسه'))
@app.on_message(filters.text & filters.regex('RESET'))
@app.on_message(filters.text & filters.regex('sptmin'))
@app.on_message(filters.text & filters.regex('aspn'))
def tag(client, message):
    global tags, tag_stop, mention, tglist, speed
    if message.text.split()[0] == 'tag':
        try:
            text = message.text[5:]
        except:
            text = ''
        tag_stop[message.chat.id] = 'False'
        result2 = app.get_chat_members(chat_id=message.chat.id)
        s = []
        while tag_stop[message.chat.id] == 'False':
            usr = random.choice(result2)
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
    elif message.text.split()[0] == 'DEL':
        try:
            app.send_message(chat_id=message.chat.id,
                                  text="```1 2 3.```")
            app.delete_messages(chat_id=message.chat.id, message_ids=tags[message.chat.id])
            app.send_message(chat_id=message.chat.id,
                                  text="```🗑tag DEL✅.```")
            tags.pop(message.chat.id)
        except:
            app.send_message(message.chat.id, '```🗑tagi nkrdm```')
    elif message.text.split()[0] == 'بسه':
        tag_stop[message.chat.id] = True
        app.send_message(chat_id=message.chat.id, text='```📌tag stop 🛑```')
    elif message.text.split()[0] == '':
        mention = ''
        tglist = ''
        app.send_message(message.chat.id, 'سپن پاکسازی شد')
    elif message.text.split()[0] == 'sptmin':
        if message.reply_to_message:
            tglist = message.reply_to_message.text
        else:
            tglist = message.text[10:]
        app.send_message(message.chat.id, '``` متن اسپن با موفقیت ثبت شد``')
    elif message.text.split()[0] == 'aspn':
        tag_stop[message.chat.id] = 'False'
        if tglist == '':
            app.send_message(message.chat.id, '```متن اسپن ثبت نشده.```')
        else:
            tag_stop[message.chat.id] = 'False'
            try:
                count = int(message.text.split()[1])
            except:
                count = -1
            users = app.iter_chat_members(message.chat.id, limit=10)
            num = 0
            s = []
            while tag_stop[message.chat.id] == 'False' and count != num:
                text = tglist
                while True:
                    randomed = random.choice(users)
                    if 'TAG' in text:
                        while True:
                            if randomed.user.is_bot or randomed.user.id == 528220205 or randomed.user.first_name == None:
                                break
                            else:
                                text = text.replace('TAG', f'tg://user?id={randomed.user.id}', 0)
                                break
                    if 'USER' in text:
                        while True:
                            if randomed.user.is_bot or randomed.user.id == 528220205 or randomed.user.first_name == None:
                                break
                            else:
                                text = text.replace('USER', f'{randomed.user.first_name}', 0)
                                break
                    else:
                        break
                hel = app.send_message(message.chat.id, text)
                s.append(hel.message_id)
                num += 1
                sleep(speed)
        try:
            u = tags[message.chat.id]
            u += s
            tags[message.chat.id] = u
        except:
            tags[message.chat.id] = s

shekar = r'#ch|#شکار|#شکارم|#شکارچی|#shekar|#shekarchi'
@app.on_message(filters.regex(shekar))
def pin_ch(client, message):
    app.pin_chat_message(message.chat.id,message.message_id)


app.run()
