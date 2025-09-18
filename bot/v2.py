#Version 1.1.2
import os, discord, tracemalloc, time, datetime
from discord.ext import commands
from dotenv import load_dotenv

########--- Main variable definitions, should not change ---##########



MAINSERVER = "Dragonkind" # outdated name, do I change?
intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('&'),
    description = "Webmaster is currently under development (v2).",
    activity = discord.Game(name=f"/help | Ready"),
    status = discord.Status.online,
    intents = intents
)
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Notes:
# Discord requires bots to use slash commands
# now. Will need to learn how that business
# works.

# On ready, print
@bot.event
async def on_ready():
    servers = bot.guilds
    print(f"Connected as {bot.user} to {len(servers)} servers:")
    for x in servers:
        print(x.name)
    tracemalloc.start()   # Got error "Runtime Warning: Enable tracemalloc to get various things"
    await bot.load_extension("cogs")
    await bot.load_extension("button")



# On command error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: \n {error}")

# For development environment
class BotFrontend(self):
	def __init__(self):
		self.bot = bot


	def start_bot_frontend(self):
		try:
			self.bot.run(token)
			return
		except Exception as inst:
			return inst

# For testing
if __name__ == "__main__":
	bot.run(token)
