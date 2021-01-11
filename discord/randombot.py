import os
import random
import discord

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_content = message.content.lower()
    if "flip a coin" in message_content:
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"
        await message.channel.send(results)

    if "roll a die" in message_content or "roll a dice" in message_content:
        rand_int = random.randint(1, 6)
        results = f"You rolled a {rand_int}"
        await message.channel.send(results)

    elif "roll a d" in message_content:
        droll = message_content.split("roll a")[1].strip().split()[0]
        try:
            sides = int(droll[1:])
        except ValueError:
            pass
        else:
            rand_int = random.randint(1, sides)
            results = f"You rolled a {rand_int}"
            await message.channel.send(results)

    if "pick a card" in message_content or "choose a card" in message_content:
        suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
        cards = [
            "Ace",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Jack",
            "Queen",
            "King",
        ]

        results = f"You picked the {random.choice(cards)} of {random.choice(suit)}"

        await message.channel.send(results)


client.run(token)
