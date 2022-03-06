from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

feri = 'BAA9WLj4NC92s0BRoKxVYHYOJYqqtxJyfNwMxSwKkZDOF-aGD7fSw7RngKE1cD6oR1kMO9AiSYK4qvctfDnnMh4hv6Yet1w_dWU1yLXvTbwWtE0EBox-E2RySFHTtw6vk0KOyqdpYc9FGxFFNPeivl0oySsEJ0elFeJMpyn-eCMPHzQujuZ6HQbtqTfGsMFo_kPOHe3fa26wRxd1x8frja3hX-ijRTQ_mqemR5IFwCcDVZLTLpAGqlcRi3HlOIXcM_Xz6NKEeymChv9rDSShkoA6nCW5CCY5StcLGbXFaw1wMUO7qZWk-6MA-mZuWjChZ3D-0M520qTF9ckrWUzo4Y5CAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

[Forwarded from یابندگان حجت]
import os ,sys 
if sys.platform == 'win32':
    ins = 'python -m pip install jdatetime pyrogram'
else:
    ins = 'pip install jdatetime pyrogram'
os.system(ins)

timer = False
last_bio = None

def job(mybio:str):
    global timer
    t = Timer(30,job,(mybio,))
    if timer:
        now = jdatetime.datetime.now().strftime('%H:%M')
        font1="1234567890"
        font2="¹²³⁴⁵⁶⁷⁸⁹⁰"
        now = now.translate(now.maketrans(font1,font2))
        my_bio = '【{}】{}'.format(now,mybio)
        t.start()
        if mybio is not None:
            app.update_profile(last_name=now) 
        else:
            app.update_profile(last_name=now)
    else:
        t.cancel()

@app.on_message(filters.command('time_bio') & filters.me)
def time_in_bio(client, message):
    global timer, last_bio
    mybio = app.get_chat(message.from_user.id).bio
    if len(message.command) == 2:
        if message.command[1].lower() == 'on':
            if timer:
                message.reply_text('فعال بود')
            else:
                timer = True
                last_bio = mybio
                job(mybio)
                message.reply_text('ok')
        if message.command[1].lower() == 'off':
            if timer:
                timer = False
                app.update_profile(bio=last_bio)
                message.reply_text('ok')
            else:
                message.reply_text('غیر فعال بود')
    
app.run()
