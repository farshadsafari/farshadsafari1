from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions
from datetime import datetime
import pytz
import aiocron
import asyncio

api_id = "2669159"
api_hash="761194071ffe6e596a71e72056a9ae73"

Client=TelegramClient("time", api_id, api_hash)

@aiocron.crontab('*/1 * * * *')
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
