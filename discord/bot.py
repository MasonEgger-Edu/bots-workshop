import os

import discord

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")
client = discord.Client()


@client.event
async def on_read():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

        print(
            f"{client.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
        )


client.run(token)
