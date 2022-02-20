from pyrogram import Client, filters
from requests import get
from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions
from datetime import datetime
import pytz
import asyncio
import pyrogram
import json
from time import sleep

pmtags = []

feri = 'BACGKl-eu7fB_b4pacZGSHbNAg3u3tQ-D_gHQr3x5pDVEloLClls9FwsXaGYvEJ_EsZuZeL7eVgwyOsYdYJVJfxuGm9pDFfRUV0bZl7n8NaFoOxDJG26I-rO3BfK6V2ChfKnNm05P7UpSR6rcZGsx74k7H9nhysPCGCqWCfRKppIZBKdTAZADFQa0dE6SPiDpXYdU7O1x-BfAdemDrVMr9ChK08c4JO4pDXyml0HNEZYYvthLOzJHPqjqcpXQ-jTKNIenfwu1GTzNM2ZidND6eEKd1b2N7IV3af1sjr0dPXAEo7cb_1Yo0NjZOWM63N6q06GCBJgkOfJ0nYhnICutq4affQeHQA'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')


@aiocron.crontab('* * * * *')
async def clock():
	ir=pytz.timezone("Asia/Tehran")
	time=datetime.now(ir).strftime("%H:%M")
	font1="1234567890"
	font2="❶➁➂➃➄６７❽９０"
	await Client(functions.account.UpdateProfileRequest(last_name=time.translate(time.maketrans(font1,font2))))

Client.start()



clock.start()
Client.run_until_disconnected()
asyncio.get_event_loop().run_forever()

app.run()
