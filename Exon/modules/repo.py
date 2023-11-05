# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Realkronos
#     MY ALL BOTS :- Spartans_mainchat
#     GITHUB :- Realkronos69 ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Exon import Abishnoi as pbot

ABISHNOIX = "https://telegra.ph/file/083b33e7d5898a6446e75.jpg"


@pbot.on_cmd("repo")
async def repo(_, message):
    await message.reply_photo(
        photo=ABISHNOIX,
        caption=f"""⚡ **ʜᴇʏ {message.from_user.mention},**

**ᴏᴡɴᴇʀ  : [𝐊ʀᴏɴᴏꜱ](https://t.me/Realkronos)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴍᴜꜱɪᴄ•", url="https://telegra.ph/file/d1f792800cf543daf2bf4.mp4"
                    ),
                    InlineKeyboardButton(
                        "•ʀᴏʙᴏᴠ1•", url="https://telegra.ph/file/d1f792800cf543daf2bf4.mp4"
                    ),
                ]
            ]
        ),
    )
