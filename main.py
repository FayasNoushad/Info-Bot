# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hello {}, I am a user info telegram bot. Send me a user id.

Made by @FayasNoushad
"""
BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )

@FayasNoushad.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@FayasNoushad.on_message(filters.private & filters.text)
async def info(bot, update):
    if int(update.text) > 0:
        user = await bot.get_users(int(update.text))
        info = user_info(bot, update, user)
    else:
        chat = await bot.get_chat(int(update.text))
        info = chat
    await update.reply_text(
        text=info,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

def user_info(user):
    text = "--**User Details:**--\n"
    text += f"\n**First Name:** `{user.first_name}`"
    text += f"\n**Last Name:** `{user.last_name},`" if user.last_name else ""
    text += f"\n**User Name:** @{user.username}" if user.username else ""
    text += f"\n**User Link:** {user.mention}" if user.username else ""
    text += f"\n**User Id:** `{user.id}`"
    text += f"\n**DC ID:** {user.dc_id}" if user.dc_id else ""
    text += f"\n**Is Verified:** `{user.is_verified}`" if user.is_verified else ""
    text += f"\n**Is Fake:** {user.is_fake}" if user.is_fake else ""
    text += f"\n**Is Scam:** {user.is_scam}" if user.is_scam else ""
    text += f"\n**Language Code:** {user.language_code}" if user.language_code else ""
    text += f"\n\nMade by @FayasNoushad"
    return text

FayasNoushad.run()
