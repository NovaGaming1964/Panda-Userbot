import asyncio
import os

from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd, sudo_cmd

PM_IMG = Config.ALIVE_PIC
version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "โฎ MY BOT IS RUNNING SUCCESFULLY โฎ"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  โฅ "

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "๐ซ๐๐ฉ๐๐-๐ฐ๐ฎ๐ธ๐๐ต๐ช๐ฏ"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/8b5c468b8552549218d8c.jpg"
file2 = "https://telegra.ph/file/8b5c468b8552549218d8c.jpg"
file3 = "https://telegra.ph/file/8b5c468b8552549218d8c.jpg"
file4 = "https://telegra.ph/file/8b5c468b8552549218d8c.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "** ๐ซ๐๐ฉ๐๐-๐ฐ๐ฎ๐ธ๐๐ต๐ช๐ฏ ๐ธ๐ ๐พ๐ฝ๐ป๐ธ๐ฝ๐ด**\n\n"

pm_caption += "โ About My System โ\n\n"
pm_caption += "โพ **`แดแดสแดแดสแดษด แด แดส๊ฑษชแดษด`** โ 1.17.5\n"
pm_caption += "โพ **`๊ฑแดแดแดแดสแด แดสแดษดษดแดส`** โ [แดแดษชษด](https://t.me/a)\n"
pm_caption += "โพ **`สษชแดแดษด๊ฑแด`**  โ [๐ซ๐๐ฉ๐๐-๐ฐ๐ฎ๐ธ๐๐ต๐ช๐ฏ](https://github.com/a)\n"
pm_caption += "โพ **`แดแดแดสสษชษขสแด สส`** โ [๐ซ๐๐ฉ๐๐-๐ฐ๐ฎ๐ธ๐๐ต๐ช๐ฏ](https://github.com/NovaGaming1964/Panda-Userbot)\n\n"
pm_caption += "โพ **Spammer Go Away Im His Assitant"
pm_caption += f"โพ **แดส แดแดsแดแดส** โ [{DEFAULTUSER}](tg://user?id={ghanti})\n"


@borg.on(lightning_cmd(pattern=r"dalive"))
@borg.on(sudo_cmd(pattern=r"dalive", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await yes.delete()

    """ For .dalive command, check if the bot is running.  """
    await borg.send_file(yes.chat_id, PM_IMG, caption=pm_caption)
    await yes.delete()
