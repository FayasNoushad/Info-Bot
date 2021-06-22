import os
from pyrogram import Client, filters

FayasNoushad = Client(
    "User-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@FayasNoushad.on_message(filters.private & filters.text)
async def user_info(bot, update):
    try:
        user = await bot.get_users(int(update.text))
        text = "--**User Details:**--\n"
        text += f"\n**First Name:** `{user.first_name}`"
        text += f"\n**Last Name:** `{user.last_name}`\n\n" if user.last_name else ""
        text += f"\n**User Name:** @{user.username}\n\n" if user.username else ""
        text += f"\n**User Link:** @{user.mention}\n\n" if user.username else ""
        text += f"\n**User Id:** `{user.id}`\n\n"
        text += f"\n**DC ID:** {user.dc_id}\n\n" if user.dc_id else ""
        text += f"\n**Is Verified:** `{user.is_verified}`\n\n" if user.is_verified else ""
        text += f"\n**Is Fake:** {user.is_fake}" if user.is_fake else ""
        text += f"\n**Is Scam:** {user.is_scam}" if user.is_scam else ""
        text += f"\n**Language Code:** {user.language_code}" if user.language_code else ""
        text += f"\n\nMade by @FayasNoushad"
        await update.reply_text(
            text=text,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(error)

FayasNoushad.run()
