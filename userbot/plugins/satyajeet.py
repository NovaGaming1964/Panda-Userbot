"""Emoji
Available Commands:
.satyajeet"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "satyajeet":

        await event.edit(input_str)

        animation_chars = [
            "░██████╗\n░█████╗░\n████████╗\n██╗░░░██╗\n░█████╗\n░░░░░░██╗\n███████╗\n███████╗\n████████╗"
            "██╔════╝\n██╔══██╗\n╚══██╔══╝\n╚██╗░██╔╝\n██╔══██╗\n░░░░░██║\n██╔════╝\n██╔════╝\n╚══██╔══╝"
            "╚█████╗\n░███████║░\n░░██║░░░░\n╚████╔╝░\n███████║\n░░░░░██║\n█████╗░░\n█████╗░░\n░░░██║░░░"
            "░╚═══██╗\n██╔══██║░░\n░██║░░░░░\n╚██╔╝░░\n██╔══██║\n██╗░░██║\n██╔══╝░░\n██╔══╝░░\n░░░██║░░░"
            "██████╔╝\n██║░░██║░░\n░██║░░░░░░\n██║░░░\n██║░░██║\n╚█████╔╝\n███████╗\n███████╗\n░░░██║░░░"
            "╚═════╝\n░╚═╝░░╚═╝░░░\n╚═╝░░░░░░\n╚═╝░░░\n╚═╝░░╚═╝\n░╚════╝░\n╚══════╝\n╚══════╝\n░░░╚═╝░░░"
            "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
            "[👉🔴👈](@Satyajeet4)",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
