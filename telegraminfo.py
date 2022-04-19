def user(user):
    text = "--**User Details:**--\n"
    text += f"\n**First Name:** `{user.first_name}`"
    text += f"\n**Last Name:** `{user.last_name},`" if user.last_name else ""
    text += f"\n**User Id:** `{user.id}`"
    text += f"\n**Username:** @{user.username}" if user.username else ""
    text += f"\n**User Link:** {user.mention}" if user.username else ""
    text += f"\n**DC ID:** `{user.dc_id}`" if user.dc_id else ""
    text += f"\n**Is Deleted:** True" if user.is_deleted else ""
    text += f"\n**Is Bot:** True" if user.is_bot else ""
    text += f"\n**Is Verified:** True" if user.is_verified else ""
    text += f"\n**Is Restricted:** True" if user.is_verified else ""
    text += f"\n**Is Scam:** True" if user.is_scam else ""
    text += f"\n**Is Fake:** True" if user.is_fake else ""
    text += f"\n**Is Support:** True" if user.is_support else ""
    text += f"\n**Language Code:** {user.language_code}" if user.language_code else ""
    text += f"\n**Status:** {user.status}" if user.status else ""
    return text


def chat(chat):
    text = "--**Chat Details**--\n" 
    text += f"\n**Title:** `{chat.title}`"
    text += f"\n**Chat ID:** `{chat.id}`"
    text += f"\n**Username:** @{chat.username}" if chat.username else ""
    text += f"\n**Type:** `{chat.type}`"
    text += f"\n**DC ID:** `{chat.dc_id}`"
    text += f"\n**Is Verified:** True" if chat.is_verified else ""
    text += f"\n**Is Restricted:** True" if chat.is_verified else ""
    text += f"\n**Is Creator:** True" if chat.is_creator else ""
    text += f"\n**Is Scam:** True" if chat.is_scam else ""
    text += f"\n**Is Fake:** True" if chat.is_fake else ""
    return text
