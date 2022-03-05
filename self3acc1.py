from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

feri = 'BAA9WLj4NC92s0BRoKxVYHYOJYqqtxJyfNwMxSwKkZDOF-aGD7fSw7RngKE1cD6oR1kMO9AiSYK4qvctfDnnMh4hv6Yet1w_dWU1yLXvTbwWtE0EBox-E2RySFHTtw6vk0KOyqdpYc9FGxFFNPeivl0oySsEJ0elFeJMpyn-eCMPHzQujuZ6HQbtqTfGsMFo_kPOHe3fa26wRxd1x8frja3hX-ijRTQ_mqemR5IFwCcDVZLTLpAGqlcRi3HlOIXcM_Xz6NKEeymChv9rDSShkoA6nCW5CCY5StcLGbXFaw1wMUO7qZWk-6MA-mZuWjChZ3D-0M520qTF9ckrWUzo4Y5CAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')


wlc_info = {}
wlc_heh = {}

@app.on_message(filters.text & filters.me & filters.regex('Setwelcome'))
def setwlc(client,message):
    global wlc_info,wlc_heh
    chat_id = message.chat.id
    if message.reply_to_message:
        wlc_heh[message.chat.id] = True
        wlc_info[chat_id] = message.reply_to_message.text
        message.reply_text("**wlc seted✅**")

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
@app.on_message(filters.text & filters.me & filters.regex('Offwelcome'))
def wlcof(clientt,message):
    global wlc_heh
    wlc_heh[message.chat.id] = False 
 
@app.on_message(filters.text & filters.me & filters.regex('Block'))
def block_users(client,message):
    user = message.reply_to_message.from_user.id
    app.block_user(user)
    message.reply_text('**User block✅**')


@app.on_message(filters.text & filters.me & filters.regex('Unblock'))
def unblock_user(client,message):
    user = message.reply_to_message.from_user.id
    app.unblock_user(user)
    message.reply_text('**User unblock✅**')
    
app.run()
