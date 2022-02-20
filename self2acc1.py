from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

pmtags = []

feri = 'BACGKl-eu7fB_b4pacZGSHbNAg3u3tQ-D_gHQr3x5pDVEloLClls9FwsXaGYvEJ_EsZuZeL7eVgwyOsYdYJVJfxuGm9pDFfRUV0bZl7n8NaFoOxDJG26I-rO3BfK6V2ChfKnNm05P7UpSR6rcZGsx74k7H9nhysPCGCqWCfRKppIZBKdTAZADFQa0dE6SPiDpXYdU7O1x-BfAdemDrVMr9ChK08c4JO4pDXyml0HNEZYYvthLOzJHPqjqcpXQ-jTKNIenfwu1GTzNM2ZidND6eEKd1b2N7IV3af1sjr0dPXAEo7cb_1Yo0NjZOWM63N6q06GCBJgkOfJ0nYhnICutq4affQeHQA'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')
  
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
