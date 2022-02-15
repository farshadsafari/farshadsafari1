from pyrogram import Client, filters
from requests import get
import pyrogram
import json
import random
from time import sleep

feri = 'BAAK-xvePWLi5TaQwYKSHX249UsL1ptjmQke25WiSk5SXJr18ANYsNxQ38ZndswDUovazfrgjmjHpvEmIrqdpmx2xjqU-sMMYs4LJ1Rl2Tb4Fwb8I62v_lPzjjSqTvCulshrMxkQQmhfccGMks-eyqGtWMWsgE9tL4GhitgIGdXtcVwdUZz9oEcy-u8CE2cYcrnZCVtmHOmvGD_bh8P1t8atYVstIKbo7B69FbFsTFRQYCXyiNa95mDcroLCAHOAS-wsUPiwMMM89VAI-cGwNBAa3uvA4iHzrd9F6Tp6xnCd8IYqE2XjKZNaF2VOvBpcm5PgbI_OQ7sAaf_tJjJ9uWWUAAAAATuwAm0A'
app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

@app.on_message(filters.command(["stats", ''],None))
def stats(c,m):
    user = m.reply_to_message.from_user
    statsuser = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={user.id}&json=true").json()
    if not statsuser:
        m.edit_text(f"**کاربر {user.mention} هیچ سابقه ای در بازی گرگینه ندارد**")
        return
    tedadbazia = statsuser["gamesPlayed"]
    tedadBord = statsuser["won"]["total"]
    darsadBord = statsuser["won"]["percent"]
    tedadBakht = statsuser["lost"]["total"]
    darsadBakht = statsuser["lost"]["percent"]
    qoflish = statsuser["mostKilled"]["name"]
    tqoflish = statsuser["mostKilled"]["times"]
    qoflit = statsuser["mostKilledBy"]["name"]
    tqoflit = statsuser["mostKilledBy"]["times"]
    m.edit_text(f"""**●┓ کاربر **{user.mention}
**●┫ شناسه کاربر:** `{user.id}`
**●┫ بازی های انجام ‌شده:** {tedadbazia}
**●┫ برد ها:** {tedadBord}
**●┫ باخت ها:** {tedadBakht}
**●┫ درصد برد:** {darsadBord}
**●┫ درصد باخت:** {darsadBakht}
**●┫ قفلیشی:** {tqoflish} | {qoflish}
**●┛ قفلیته:** {tqoflit} | {qoflit}
""")

@app.on_message(filters.command(["kills"],None))
def kills(c,m):
    user = m.reply_to_message.from_user
    killsuser = get(f"https://Tgwerewolf.com/stats/PlayerKills/?pid={user.id}&json=true").json()
    if not killsuser:
        m.edit_text(f"**کاربر {user.mention} هیچ سابقه ای در بازی گرگینه ندارد**")
        return
    number1 = killsuser[0]["name"]
    number1tedad = killsuser[0]["times"]
    number2 = killsuser[1]["name"]
    number2tedad = killsuser[1]["times"]
    number3 = killsuser[2]["name"]
    number3tedad = killsuser[2]["times"]
    number4 = killsuser[3]["name"]
    number4tedad = killsuser[3]["times"]
    number5 = killsuser[4]["name"]
    number5tedad = killsuser[4]["times"]
    m.edit_text(f"""**لیست کشتار **{user.mention}:
**●┓{number1tedad}**  |  {number1}    
**●┫{number2tedad}**  |  {number2}
**●┫{number3tedad}**  |  {number3}
**●┫{number4tedad}**  |  {number4}
**●┛{number5tedad}**  |  {number5}
""")

@app.on_message(filters.command(["killedby"],None))
def killedby(c,m):
    user = m.reply_to_message.from_user
    killedbyusr = get(f"https://Tgwerewolf.com/stats/Playerkilledby/?pid={user.id}&json=true").json()
    if not killedbyusr:
        m.edit_text(f"**کاربر {user.mention} هیچ سابقه ای در بازی گرگینه ندارد**")
        return
    fard1 = killedbyusr[0]["name"]
    mqdar1 = killedbyusr[0]["times"]
    fard2 = killedbyusr[1]["name"]
    mqdar2 = killedbyusr[1]["times"]
    fard3 = killedbyusr[2]["name"]
    mqdar3 = killedbyusr[2]["times"]
    fard4 = killedbyusr[3]["name"]
    mqdar4 = killedbyusr[3]["times"]
    fard5 = killedbyusr[4]["name"]
    mqdar5 = killedbyusr[4]["times"]
    m.edit_text(f"""**لیست قاتلان **{user.mention}:
**●┓{mqdar1}**  |  {fard1}    
**●┫{mqdar2}**  |  {fard2}
**●┫{mqdar3}**  |  {fard3}
**●┫{mqdar4}**  |  {fard4}
**●┛{mqdar5}**  |  {fard5}
""")

app.run()
