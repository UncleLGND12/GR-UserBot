#Port By @VckyouuBitch From GeezProjects
#Copyright © 2021 Geez-Projects
from telethon.tl.types import (
    ChannelParticipantsKicked,
)

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.allunban(?: |$)(.*)", groups_only=True)
async def _(event):
    await event.edit("`Searching Participant Lists.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit(f"`{title}: {p} UnBanned`")


CMD_HELP.update(
    {
        "allunban": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.allunban`\
    \n↳ : Membatalkan semua Ban Di Anggota Grup."
    }
)
