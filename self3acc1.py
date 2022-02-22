from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import random
from time import sleep
import redis 
import asyncio 

feri = 'BAAXPuF3nwc9gydVBfwKY_UFrsqGiZINDeCeh6gvKiXQPPq5cQzgq3HtKLsjf7JfIyG5h7POob2zNvIZzVM8STWcx07NtTYZmLvA7hlYEFH5cqBnBp-_7I4ErkGm5_sQZvQEYEwj1NDKwPXBMKQTD4VDXG_cXpaMgCVoDAtPCkeBw_JKJnB0jLMozOuNPSvDon53AACrS7SPunO2ZTSYCxK-NdzrlzeRsKMbkU4xctzhPvCa0y9Lxk_Dg2n6O5_CA6xYvltk-B1jgdo7AXbBMQ88U3xf_bRiPU5JQBf4fBdDtBOzsAM7geOot-JevCKyjn-BH1OVxorxiTMNWA9aLmPDffQeHQA'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')


try:
    import socks #pip install socks 
    proxy = (socks.SOCKS5, '127.0.0.1', 9150) #start tor
    client = TelegramClient(phone, api_id, api_hash,proxy=proxy)
    client.connect()
except:
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()


if not client.is_user_authorized(): 
    try:
        client.send_code_request(phone) 
        client.sign_in(code=input('Your Code :')) 
    except SessionPasswordNeededError:
        client.sign_in(password=input('your Password :'))
        
admin = [2113150493]
bot_id = [198626752,175844556]
group_id = int(input("-1001745227060"))
print("▓█████▄ ▓█████ ▄▄▄      ▓█████▄  ▄▄▄▄    ▒█████ ▓██   ██▓")
print("▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌▓█████▄ ▒██▒  ██▒▒██  ██▒")
print("░██   █▌▒███  ▒██  ▀█▄  ░██   █▌▒██▒ ▄██▒██░  ██▒ ▒██ ██░")
print("░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌▒██░█▀  ▒██   ██░ ░ ▐██▓░")
print("░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓ ░▓█  ▀█▓░ ████▓▒░ ░ ██▒▓░")
print(" ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒ ░▒▓███▀▒░ ▒░▒░▒░   ██▒▒▒")
print(" ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒ ▒░▒   ░   ░ ▒ ▒░ ▓██ ░▒░")
print(" ░ ░  ░    ░    ░   ▒    ░ ░  ░  ░    ░ ░ ░ ░ ▒  ▒ ▒ ░░ ")
print("   ░       ░  ░     ░  ░   ░     ░          ░ ░  ░ ░    ")
print(" ░                       ░            ░          ░ ░    ")
print("\t\tBot Loaded ")
ss = ""

data_base = {'shkar':0,'ray':'','naghsh':'','ghofli':'','ros':0,'fereshte':0,'karagah':0,'pishgo':0,'negahbani':''}
me = client.get_me()
redis.set(me.id,str(data_base))

async def main():
    @client.on(events.NewMessage(pattern=r'/ping'))
    async def shekar_1(event):
        if event.chat_id == group_id:
            if event.sender_id in admin:
                await event.reply('online')

    @client.on(events.NewMessage(pattern=r'#شکار'))
    async def shekar_1(event):
        if event.chat_id == group_id:
            try:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['shkar'] = event.sender_id
                redis.set(me.id,str(get_list))
            except Exception as e:
                print(e)
    
    @client.on(events.NewMessage(pattern=r'#شکارچی'))
    async def shekar_2(event):
        if event.chat_id == group_id:
            try:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['shkar'] = event.sender_id
                redis.set(me.id,str(get_list))
            except Exception as e:
                print(e)
    
    @client.on(events.NewMessage(pattern=r'#شکارم'))
    async def shekar_3(event):
        if event.chat_id == group_id:
            try:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['shkar'] = event.sender_id
                redis.set(me.id,str(get_list))
            except Exception as e:
                print(e)
    
    @client.on(events.NewMessage(pattern=r'#shekar'))
    async def shekar_4(event):
        if event.chat_id == group_id:
            try:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['shkar'] = event.sender_id
                redis.set(me.id,str(get_list))
            except Exception as e:
                print(e)
    
    @client.on(events.NewMessage(pattern=r'تو شکارچی هستی‌'))
    async def shekar_5(event):
        if event.sender_id in bot_id:
            await client.send_message(int(group_id),"#شکار")
  
    @client.on(events.NewMessage(pattern=r'بازیکن های زنده:'))
    async def list_naghsh_user(event):  
        if event.chat_id == group_id:
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            get_list['naghsh'] = ''
            try:
                ssw = await client.get_entity('me')
                for i in event.text.split("\n"):
                    if ': 🙂 زنده' in i:
                        if not ssw.first_name in i:
                            if not i == "":
                                try:
                                    get_list['naghsh'] += str(i.split('[')[1].split(']')[0])+"\n"
                                except Exception as e:
                                    print(e)
                redis.set(me.id,str(get_list))
            except Exception as e:
                print(e)

    @client.on(events.NewMessage(pattern=r'یک بازی با حالت'))
    async def start_ganme(event):
        if event.chat_id == group_id:
            if event.sender_id in bot_id:
                text_url = await client.get_messages(event.chat_id)
                bot_ids = event.sender_id
                text_url = str(text_url[0].reply_markup).split("start=")[1].split("'")[0]
                await client.send_message(bot_ids,"/start "+text_url)
                await asyncio.sleep(2) 
                await client.send_message(bot_ids,"/start "+text_url)
                await asyncio.sleep(2) 
                await client.send_message(bot_ids,"/start "+text_url)
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['shkar'] = 0
                get_list['ros'] = 0
                get_list['karagah'] = 0
                get_list['fereshte'] = 0
                get_list['pishgo'] = 0
                get_list['negahbani'] = ''
                get_list['naghsh'] = ''
                get_list['ray'] = ''
                redis.set(me.id,str(get_list))
    
    @client.on(events.NewMessage(pattern=r'تو یه روستایی ساده ای🙂'))
    async def rose(event):
        if event.sender_id in bot_id:
            await asyncio.sleep(4)
            await client.send_message(int(group_id),"روستایی\n\n\nسادم نیاب افکم")
            await client.send_message(int(group_id),"/sn ros")
    
    @client.on(events.NewMessage(pattern=r'دیشب تاریک بود و فاحشه اومد یه حالی بهت داد و رفت!'))
    async def faheshe_gane(event):
        if event.sender_id in bot_id:
            await asyncio.sleep(4) 
            text = ['مرسی فاحشه','بازم سر بهم بزن فاحشه','کجا بودی زودتر میومدی پیشم فاحشه','سیف فاحشم','faheshe omad man','safe fahesham','bos faheshe','فاحشه بیشتر بیا پیشم']
            text = text[random.randint(0,len(text)-1)]
            await client.send_message(int(group_id),text)
    
    @client.on(events.NewMessage(pattern=r'ای شیطون! میخوای بری خونه کی؟'))
    async def faheshe(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(4)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await client.send_message(int(group_id),"رفتم \n"+ss)
            await s[0].click(text=ss)
    
    @client.on(events.NewMessage(pattern=r'کیو میخوای ببینی؟'))
    async def pishgo(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(4)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)

    @client.on(events.NewMessage(pattern=r'کیو میخوای بخوری؟'))
    async def gorg(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(4)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            print(list_naghsh)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)

    @client.on(events.NewMessage(pattern=r'کیو میخوای شکار کنی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            get_list['shkar'] = 200
            redis.set(me.id,str(get_list))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await client.send_message(int(group_id),"میرم شکار {0}".format(ss))
    
    @client.on(events.NewMessage(pattern=r'الگوت کی باشه؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss) 
  
    @client.on(events.NewMessage(pattern=r'به کی میخوای تیر بزنی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await client.send_message(int(group_id),"بای بای کن {0}".format(ss))
            await s[0].click(text=ss) 

    @client.on(events.NewMessage(pattern=r'کیو میخوای عضو انجمنت کنی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)

    @client.on(events.NewMessage(pattern=r'میخوای همزاد کی بشی؟ اگه بمیره تو نقششو بر عهده میگیری'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            
            await s[0].click(text=ss) 
            
    @client.on(events.NewMessage(pattern=r'کیو میخوای امشب بکشی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss) 

    @client.on(events.NewMessage(pattern=r'کیا رو میخوای عاشق همدیگه بکنی؟ نفر اول رو انتخاب کن'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(10)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)

    @client.on(events.NewMessage(pattern=r'کیا رو میخوای عاشق همدیگه بکنی؟ نفر دوم رو انتخاب کن'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)

    @client.on(events.NewMessage(pattern=r'نقش کیو میخوای بدزدی؟😈'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)

    @client.on(events.NewMessage(pattern=r'امشب کی میتونه یه میزبان و شریک خوب توی شرط بندی باشه؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)
            
    @client.on(events.NewMessage(pattern=r'میخوای امشب کی رو منجمد کنی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text=ss)
            
    @client.on(events.NewMessage(pattern=r'میخوای یه خونه دیگه رو هم آغشته کنی یا میخوای با یه جرقه همشون رو بسوزونی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(6)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            try:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    for i in get_list['naghsh'].split("\n"):
                        if not shekar.first_name in i:
                            list_naghsh.append(i)
                else :
                    for i in get_list['naghsh'].split("\n"):
                        list_naghsh.append(i)
            except Exception as e:
                print(e)
            random_id = random.randint(0,len(list_naghsh))
            s = await client.get_messages(event.chat_id)
            ss = list_naghsh[random_id]
            await s[0].click(text='جرقه')
            await asyncio.sleep(2)
            await s[0].click(text=ss)
    
    @client.on(events.NewMessage(pattern=r'اگه برای اعلام کردن نقشت آماده هستی روی "اعلام کردم" کلیک کن تا بتونی از این به بعد 2 تا رای بدی😁'))
    async def ros(event):
        if event.sender_id in bot_id:
            s = await client.get_messages(event.chat_id)
            await s[0].click(text="اعلام کردن")
            
    @client.on(events.NewMessage(pattern=r'دوست داری امشب توی هوا نقره پخش کنی و روستارو از دست گرگ ها نجات بدی؟!'))
    async def ros(event):
        if event.sender_id in bot_id:
            s = await client.get_messages(event.chat_id)
            await s[0].click(text="آره")
            
    @client.on(events.NewMessage(pattern=r'میخوای امشب همه رو به خواب ببری؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            s = await client.get_messages(event.chat_id)
            await s[0].click(text="آره")
            
    @client.on(events.NewMessage(pattern=r'این دکمه رو فشار بده ویه سخنرانی در مورد حقوق بشر بکن، یادت باشه وقتی این کار رو بکنی جلوی رای دادن روستا رو میگیری و کسی اعدام نمیشه 😐'))
    async def ros(event):
        if event.sender_id in bot_id:
            s = await client.get_messages(event.chat_id)
            await s[0].click(text="صلح!")

    async def sabtnaghs(text):
        await asyncio.sleep(10)
        await client.send_message(int(group_id),text)
            
    @client.on(events.NewMessage)
    async def sabtnaghsha(event):
        if event.sender_id in bot_id:
            if 'تو شکارچی هستی‌' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn شکار')
            elif 'تو  صلح گرا هستی☮️' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn صلح')
            elif 'تو بچه وحشی هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn وحشی')
            elif 'تو ناظر هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn ناظر')
            elif 'تو الان آقا گرگه ای!' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                text = ['روس','بی ازار تر از منم هست مگه','مست','گورکن','گیج','الهه','فرا','رمال']
                text = text[random.randint(0,len(text)-1)]
                await asyncio.sleep(10)
                await sabtnaghs('/sn {0}'.format(text))
            elif 'الکلی بدبخت!‌' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn مست')
            elif 'تو گورکن هستی ☠️' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn گورکن')
            elif 'تو قاتل زنجیره ای هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                text = ['روس','بی ازار تر از منم هست مگه','مست','گورکن','گیج','الهه','فرا','رمال']
                text = text[random.randint(0,len(text)-1)]
                await asyncio.sleep(10)
                await sabtnaghs('/sn {0}'.format(text))
            elif '‌خائن کثیف!' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif '‌تو رمال هستی 🦅' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn رمال')
            elif 'تو همزادی!' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 0
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn همزاد')
            elif 'تو گرگ برفی هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                text = ['روس','بی ازار تر از منم هست مگه','مست','گورکن','گیج','الهه','فرا','رمال']
                text = text[random.randint(0,len(text)-1)]
                await asyncio.sleep(10)
                await sabtnaghs('/sn {0}'.format(text))
            elif 'تو کدخدا' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn کدخدا')
            elif 'تو فرشته نگهبانی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                if not get_list['shkar'] == 0:
                    await client.send_message(get_list['shkar'],'من فرشته ام')
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو تفنگدار هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو گرگ نمایی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn گرگنما')
            elif 'تو یه شیمیدان' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو پیشگو هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                if not get_list['shkar'] == 0:
                    await client.send_message(get_list['shkar'],'من پیشگوام')
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو ریش سفیدی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn ریش')
            elif 'تو آتش زن هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                text = ['روس','بی ازار تر از منم هست مگه','مست','گورکن','گیج','الهه','فرا','رمال']
                text = text[random.randint(0,len(text)-1)]
                await asyncio.sleep(10)
                await sabtnaghs('/sn {0}'.format(text))
            elif 'تو فراماسونی ' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn فرا')
            elif 'تو پسر گیجی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn گیج')
            elif 'تو یه روستایی ساده ای🙂' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو کاراگاهی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                if not get_list['shkar'] == 0:
                    await client.send_message(get_list['shkar'],'من کاراگاهم')
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو شاهزاده ای' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn شاهزاده')
            elif 'تو فرقه گرا  هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو کلانتر روستا هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn کلانتر')
            elif 'تو دردسرسازی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn دردسر')
            elif 'تو فاحشه ای ' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn فاحشه')
            elif 'تو الهه عشقی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn الهه')
            elif 'تو توله گرگ' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 2
                redis.set(me.id,str(get_list))
                text = ['روس','بی ازار تر از منم هست مگه','مست','گورکن','گیج','الهه','فرا','رمال']
                text = text[random.randint(0,len(text)-1)]
                await asyncio.sleep(10)
                await sabtnaghs('/sn {0}'.format(text))
            elif 'تو خواب گذار هستی' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'تو آهنگری' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ros'] = 1
                redis.set(me.id,str(get_list))
                await asyncio.sleep(10)
                await sabtnaghs('/sn روس')
            elif 'جالبه بدونی' in event.text:
                if 'نقشش' in event.text:
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    if not get_list['shkar'] == 0:
                        await client.send_message(int(get_list['shkar']),event.message.message)
                    else :
                        messag = event.message.message
                        print(type(messag))
                        messag = messag.strip('جالبه بدونی')
                        messag = messag.strip('نقشش')
                        await client.send_message(group_id,messag)
            elif 'تو دیدی که' in event.text:
                if 'نیست.' in event.text:
                    messag = event.message.message
                    print(type(messag))
                    messag = messag.strip('تو دیدی که')
                    messag = messag.strip('،')
                    messag = messag.strip('.')
                    await client.send_message(group_id,messag)
            elif 'نتیجه تحقیقات تو نشون میده' in event.text:
                if 'چیزی نیست جز' in event.text:
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    if not get_list['shkar'] == 0:
                        await client.send_message(int(get_list['shkar']),event.message.message)
                    else :
                        messag = event.message.message
                        print(type(messag))
                        messag = messag.strip('نتیجه تحقیقات تو نشون میده')
                        messag = messag.strip('چیزی نیست جز')
                        await client.send_message(group_id,messag)
            elif 'همانطور که به آسمان نگاه میکنید' in event.text:
                if 'توی روستا نیست' in event.text:
                    messag = event.message.message
                    print(type(messag))
                    messag = messag.strip('همانطور که به آسمان نگاه میکنید متوجه فرم عجیب پرنده ها میشوید. این فقط میتونه به این معنی باشه که ')
                    await client.send_message(group_id,messag)

    @client.on(events.NewMessage(func=lambda e: e.is_private))
    async def pv_get(event):
        if event.text == 'من پیشگوام':
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            get_list['pishgo'] = event.sender_id
            redis.set(me.id,str(get_list))
            await event.reply('حله')
        elif event.text == 'من فرشته ام':
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            get_list['karagah'] = event.sender_id
            redis.set(me.id,str(get_list))
            await event.reply('حله')
        elif event.text == 'من کاراگاهم':
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            get_list['fereshte'] = event.sender_id
            redis.set(me.id,str(get_list))
            await event.reply('حله')
        elif 'جالبه بدونی' in event.text:
            if 'نقشش فرقه گرا 👤' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش فرقه گرا 👤 هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'جالبه بدونی' in event.text:
            if 'گرگ برفی 🐺☃️' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش  گرگ برفی 🐺☃️  هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'جالبه بدونی' in event.text:
            if 'نقشش جادوگر 🔮' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش جادوگر 🔮 هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'جالبه بدونی' in event.text:
            if 'نقشش خائن 🖕' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش خائن 🖕 هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'جالبه بدونی' in event.text:
            if 'گرگینه 🐺' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش گرگینه 🐺 هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'جالبه بدونی' in event.text:
            if 'نقشش 🔪قاتل زنجیره ای' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش 🔪قاتل زنجیره ای هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'جالبه بدونی' in event.text:
            if 'نقشش  آتش زن 🔥' in event.text:
                messag = event.message.message
                messag = messag.strip('جالبه بدونی ')
                messag = messag.strip(' نقشش  آتش زن 🔥 هستش')
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['ray'] == messag
                redis.set(me.id,str(get_list))
                await client.send_message(group_id,'/sv {0}'.format(messag))
        elif 'از کی میخوای نگهبانی کنی؟' == event.text:
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            if not get_list['karagah'] == 0:
                player = await client.get_entity(get_list['karagah'])
                await client.send_message(event.sender_id,'نگهبانی کن از {0}'.format(player.first_name))
            elif not get_list['pishgo'] == 0:
                player = await client.get_entity(get_list['pishgo'])
                await client.send_message(event.sender_id,'نگهبانی کن از {0}'.format(player.first_name))
        elif 'نگهبانی کن از ' in event.text:
            if '@' in event.text:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                if not get_list['shkar'] == 0:
                    if event.sender_id == get_list['shkar']:
                        messag = event.message.message
                        messag = messag.strip('نگهبانی کن از ')
                        messag = messag.strip('@')
                        try:
                            ssw = await client.get_entity(messag)
                            get_list['negahbani'] = ssw.first_name
                            redis.set(me.id,str(get_list))
                        except Exception as e:
                            print(e)
            else:
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                if not get_list['shkar'] == 0:
                    if event.sender_id == get_list['shkar']:
                        messag = event.message.message
                        messag = messag.strip('نگهبانی کن از ')
                        get_list['negahbani'] = messag
                        redis.set(me.id,str(get_list))
        elif 'نتیجه تحقیقات تو نشون میده' in event.text:
            if 'چیزی نیست جز' in event.text:
                if 'آتش زن' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز  آتش زن 🔥')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'توله گرگ' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز توله گرگ 🐶')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'نفرین' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز نفرین شده 😾')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'گرگ برفی ' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز  گرگ برفی 🐺☃️')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'گرگ آلفا' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز گرگ آلفا ⚡️')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'خائن' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز خائن 🖕')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'فرقه گرا' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز فرقه گرا 👤')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'گرگ ایکس' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز گرگ ایکس 🐺🌝')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif 'گرگینه' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز گرگینه 🐺')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
                elif '🔪قاتل' in event.text:
                    messag = event.message.message
                    messag = messag.strip('نتیجه تحقیقات تو نشون میده که ')
                    messag = messag.strip(' چیزی نیست جز 🔪قاتل زنجیره ای')
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    get_list['ray'] == messag
                    redis.set(me.id,str(get_list))
                    await client.send_message(group_id,'/sv {0}'.format(messag))
    
    @client.on(events.NewMessage(pattern=r'/sv'))
    async def sv_ros(event):
        if event.chat_id == group_id:
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            if not get_list['shkar'] == 0:
                if get_list['ros'] == 1:
                    messag = event.message.message
                    messag = messag.strip('/sv ')
                    if '@' in messag:
                        messag = messag.strip('@')
                        try:
                            ssw = await client.get_entity(messag)
                            get_list['ray'] = ssw.first_name
                            redis.set(me.id,str(get_list))
                        except Exception as e:
                            print(e)
                    else:
                        get_list['ray'] == messag
                        redis.set(me.id,str(get_list))
                
    @client.on(events.NewMessage(pattern=r'از کی میخوای نگهبانی کنی؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            list_naghsh = []
            await asyncio.sleep(28)
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            if not get_list['negahbani'] == '':
                s = await client.get_messages(event.chat_id)
                await s[0].click(text=get_list['negahbani'])
            elif not get_list['shkar'] == 0:
                if not get_list['shkar'] == 0:
                    shekar = await client.get_entity(int(get_list['shkar']))
                    s = await client.get_messages(event.chat_id)
                    await s[0].click(text=shekar.first_name)
            else:
                try:
                    if not get_list['shkar'] == 0:
                        shekar = await client.get_entity(int(get_list['shkar']))
                        for i in get_list['naghsh'].split("\n"):
                            if not shekar.first_name in i:
                                list_naghsh.append(i)
                    else :
                        for i in get_list['naghsh'].split("\n"):
                            list_naghsh.append(i)
                except Exception as e:
                    print(e)
                random_id = random.randint(0,len(list_naghsh))
                s = await client.get_messages(event.chat_id)
                ss = list_naghsh[random_id]
                await s[0].click(text=ss)
    
    @client.on(events.NewMessage(pattern=r'به کی رای میدی که اعدام بشه؟'))
    async def ros(event):
        if event.sender_id in bot_id:
            me = await client.get_me()
            get_list = redis.get(me.id)
            get_list = eval(get_list.decode('utf-8'))
            if get_list['ros'] == 1:
                if get_list['ray'] == '':
                    list_naghsh = []
                    await asyncio.sleep(4)
                    me = await client.get_me()
                    get_list = redis.get(me.id)
                    get_list = eval(get_list.decode('utf-8'))
                    try:
                        if not get_list['shkar'] == 0:
                            shekar = await client.get_entity(int(get_list['shkar']))
                            for i in get_list['naghsh'].split("\n"):
                                if not shekar.first_name in i:
                                    list_naghsh.append(i)
                        else :
                            for i in get_list['naghsh'].split("\n"):
                                list_naghsh.append(i)
                    except Exception as e:
                        print(e)
                    random_id = random.randint(0,len(list_naghsh))
                    s = await client.get_messages(event.chat_id)
                    ss = list_naghsh[random_id]
                    await client.send_message(int(group_id),"رای \n"+ss)
                    await s[0].click(text=ss)
                else:
                    s = await client.get_messages(event.chat_id)
                    await s[0].click(text=get_list['ray'])
                    get_list['ray'] == ''
                    redis.set(me.id,str(get_list))
            else:
                list_naghsh = []
                await asyncio.sleep(4)
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                try:
                    if not get_list['shkar'] == 0:
                        shekar = await client.get_entity(int(get_list['shkar']))
                        for i in get_list['naghsh'].split("\n"):
                            if not shekar.first_name in i:
                                list_naghsh.append(i)
                    else :
                        for i in get_list['naghsh'].split("\n"):
                            list_naghsh.append(i)
                except Exception as e:
                    print(e)
                random_id = random.randint(0,len(list_naghsh))
                s = await client.get_messages(event.chat_id)
                ss = list_naghsh[random_id]
                await client.send_message(int(group_id),"رای \n"+ss)
                await s[0].click(text=ss)
                    
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
client.start()
client.run_until_disconnected() 
