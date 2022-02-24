import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "OTA4NDYyOTk3Njg3NjYwNTc0.YY2GGQ.LEUkkQfBZyy0y0dJ0wNbJlv1yhI"
SERVER = "Dragonkind"
client = discord.Client()

channel = client.get_channel(945444469979897866)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
                if message.content.startswith('&'):
                        print(f"{message.author.name} used a command.")
                        print(message.content)
                        command = message.content.split("&")
                        parameters = command[1].split(" ")
                if command[1] == "doit":
                        await message.channel.send("Dewit Dewit.")
                        await message.channel.send("Yuh huh. You did it.")
                elif command[1] == "help":
                        await message.channel.send('''
Here's the rundown of Dragonkind:
---------------------------------
& is this bot's prefix. If you use it with a command that I know, then I'll
respond. Thank goodness, too!

Use "&commands" to get a list of my commands.
Get me for your own server:
https://discord.com/api/oauth2/authorize?client_id=908462997687660574&permissions=8&scope=bot
''')
                elif command[1] == "repeat":
                        await message.channel.send(str(parameters)+"\n"*10)
                        await message.channel.send("You got rolled. Do it again.")
client.run(TOKEN)
