from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

    
HELP_PIC = "https://telegra.ph/file/87f1fb4d1ab2e95cfcfe.jpg"

RiZoeLX = "🔥 𝑀𝐴𝑀𝐵𝐴 𝑋 𝑆𝑃𝐴𝑀 🔥\n\n"
 
RiZoeLX += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ__\n\n"

RiZoeLX += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n `.setname` - to change Name\n .`inviteall` - to add members using spam bots\n .`restart` - to restart all spam bots\n\n"
 
RiZoeLX += f" ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.join` - to join public channel/groups\n `.pjoin` - to join public channel/groups\n `.leave` - to leave public/private channel/groups\n\n"
 
RiZoeLX += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.delayspam` - this cmd use for delay spam\n\n"
 
RiZoeLX += f"ALL CMDS WITH DETAILS [HERE.](https://t.me/MAMBA_NETWORK)\n\n"
 
RiZoeLX += f"© @MAMBA_NETWORK | @ITZ_SUKHI\n"


@Riz.on(events.NewMessage(pattern=r"\.help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=RiZoeLX)                                                         
