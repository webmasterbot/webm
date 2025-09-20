#Version 1.1.2
import os, discord, tracemalloc, time, datetime
import logging
from discord.ext import commands
from dotenv import load_dotenv

logging.basicConfig(filename="botLog.txt", filemode="w", level=logging.INFO)
logger = logging.getLogger(__name__)

bot = commands.Bot(
    command_prefix = "&",
    description = "Webmaster is currently under development (v2).",
    activity = discord.Game(name=f"/help | Ready"),
    status = discord.Status.online,
    intents = discord.Intents.default()
)
load_dotenv()
token = os.getenv('BOT_TOKEN')

if bot and token:
	logger.info("Bot and token initialized")
else:
	logger.critical("Either bot or token not initilized!")


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



# For setting up the slash command structure.
async def setup_hooks():
	guild = discord.Object(id=918230746269880430) # Webmaster server ID
	await bot.tree.sync(guild=guild)
bot.setup_hook = setup_hooks



# On command error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: \n {error}")



# For development environment
async def startFromFlask():
	async with bot:
		await bot.load_extension("bot.cogs.test")
		await bot.start(token)

async def start():
	async with bot:
		await bot.load_extension("cogs.test")
		await bot.start(token)

# For testing
if __name__ == "__main__":
	import asyncio
	asyncio.run(start())
