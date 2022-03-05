from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

feri = 'BAA9WLj4NC92s0BRoKxVYHYOJYqqtxJyfNwMxSwKkZDOF-aGD7fSw7RngKE1cD6oR1kMO9AiSYK4qvctfDnnMh4hv6Yet1w_dWU1yLXvTbwWtE0EBox-E2RySFHTtw6vk0KOyqdpYc9FGxFFNPeivl0oySsEJ0elFeJMpyn-eCMPHzQujuZ6HQbtqTfGsMFo_kPOHe3fa26wRxd1x8frja3hX-ijRTQ_mqemR5IFwCcDVZLTLpAGqlcRi3HlOIXcM_Xz6NKEeymChv9rDSShkoA6nCW5CCY5StcLGbXFaw1wMUO7qZWk-6MA-mZuWjChZ3D-0M520qTF9ckrWUzo4Y5CAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')


@app.on_message(filters.me & filters.text & filters.command(['joingroup']) & filters.reply)
def join(client, message):
    try:
        join = message.reply_to_message.text
        client.join_chat(join)
        message.edit_text("• Joined!")
    except:
        pass
    
app.run()
