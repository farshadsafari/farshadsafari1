from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

feri = 'BAAXPuF3nwc9gydVBfwKY_UFrsqGiZINDeCeh6gvKiXQPPq5cQzgq3HtKLsjf7JfIyG5h7POob2zNvIZzVM8STWcx07NtTYZmLvA7hlYEFH5cqBnBp-_7I4ErkGm5_sQZvQEYEwj1NDKwPXBMKQTD4VDXG_cXpaMgCVoDAtPCkeBw_JKJnB0jLMozOuNPSvDon53AACrS7SPunO2ZTSYCxK-NdzrlzeRsKMbkU4xctzhPvCa0y9Lxk_Dg2n6O5_CA6xYvltk-B1jgdo7AXbBMQ88U3xf_bRiPU5JQBf4fBdDtBOzsAM7geOot-JevCKyjn-BH1OVxorxiTMNWA9aLmPDffQeHQA'

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
