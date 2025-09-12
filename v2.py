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


#####################---- DO NOT CHANGE ANYTHING ----####################

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

# Process commands
# Deprecated! Bots use slash commands now,
# so I'll need to figure that out :/
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('&'):
        await bot.process_commands(message)

# On command error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: \n {error}")


@bot.event
async def on_guild_join(guild):
    print(f"Webmaster has joined a new server\n Name: {guild.name} \n ID: {guild.id}")

@bot.event
async def on_member_ban(server, user):
    if server.name != MAINSERVER:
        return
    else:
        return f"""
Member banned:
{member.user}
{member.discriminator}"""
bot.run(token)
