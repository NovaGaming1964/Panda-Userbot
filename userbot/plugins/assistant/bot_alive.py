

import os
from telethon import events, Button, custom
from userbot.thunderconfig import Config

from userbot import ALIVE_NAME, bot 

currentversion = "2.1"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ᴘᴀɴᴅᴀ-ᴜꜱᴇʀʙᴏᴛ"
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
     PM_IMG = "https://telegra.ph/file/8b5c468b8552549218d8c.jpg"
else:
     PM_IMG = ASSIS_PIC


pm_caption = " ►**ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "► **SYSTEMS STATS**\n"
pm_caption += "► **Telethon Version:** `1.15.0` \n"
pm_caption += f"► **Assistant Version** : `{currentversion}`\n"
pm_caption += f"► **My Master** : {DEFAULTUSER} \n"
light = [[Button.url("✧Repos✧", "https://github.com/NovaGaming1964/Panda-Userbot"), Button.url("✧Support✧", "https://t.me/a")]]
light +=[[custom.Button.inline("✧Help✧", data="gibcmd")]]
@tgbot.on(events.NewMessage(pattern="^/alive" , func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
