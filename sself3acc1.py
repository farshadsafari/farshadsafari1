from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions
from datetime import datetime
import pytz
import aiocron
import asyncio

feri = 'BAAXPuF3nwc9gydVBfwKY_UFrsqGiZINDeCeh6gvKiXQPPq5cQzgq3HtKLsjf7JfIyG5h7POob2zNvIZzVM8STWcx07NtTYZmLvA7hlYEFH5cqBnBp-_7I4ErkGm5_sQZvQEYEwj1NDKwPXBMKQTD4VDXG_cXpaMgCVoDAtPCkeBw_JKJnB0jLMozOuNPSvDon53AACrS7SPunO2ZTSYCxK-NdzrlzeRsKMbkU4xctzhPvCa0y9Lxk_Dg2n6O5_CA6xYvltk-B1jgdo7AXbBMQ88U3xf_bRiPU5JQBf4fBdDtBOzsAM7geOot-JevCKyjn-BH1OVxorxiTMNWA9aLmPDffQeHQA'
tag_stop = {};tags = {};mention = '';tglist = '';speed = 1


app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

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
