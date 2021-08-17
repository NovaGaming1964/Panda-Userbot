import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd

LIGHTNING_ALV_IMG = os.environ.get("LIGHTNING_ALV_IMG", None)
if not LIGHTNING_ALV_IMG:
    LIGHTNING_ALV_IMG = "https://telegra.ph/file/d2e9f3128bf34a660a693.mp4"



version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        kirsh += time_list.pop() + ", "

    time_list.reverse()
    kirsh += ":".join(time_list)

    return kirsh

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ᴘᴀɴᴅᴀ-ᴜꜱᴇʀʙᴏᴛ"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"


from userbot import CMD_LIST

pm_caption = "**ᴘᴀɴᴅᴀ ᴜꜱᴇʀʙᴏᴛ is online**\n\n"
pm_caption += f"★ **Boss**            : {DEFAULTUSER}\n"
pm_caption += "★ **Version**        : 1.17.5\n"
pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n┃┃━┃┃━━━━┃┃━┃┃━━━━━\n┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃\n┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃\n┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/a)"

@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, file=LIGHTNING_ALV_IMG, caption=pm_caption, link_preview=False)
    await alive.delete()
