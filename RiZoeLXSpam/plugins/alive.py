from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/87f1fb4d1ab2e95cfcfe.jpg"
  

          
rizoel = "✧ 𝑀𝐴𝑀𝐵𝐴 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑆 𝐻𝐸𝑅𝐸 "𝑀𝐴𝑀𝐵𝐴 𝑁𝐸𝑇𝑊𝑂𝑅𝐾" ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **𝑀𝐴𝑀𝐵𝐴 ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"
    
rizoel += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/MAMBA_X_SUPPORT)\n"

rizoel += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/MAMBA_NETWORK)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/SUKHPAL443/MambaLXSpam) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
