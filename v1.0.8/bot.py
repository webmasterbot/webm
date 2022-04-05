#Version 1.0.8
import os, random, requests, discord, datetime, time, sys
from discord.ext import commands
from discord.utils import *
import os
from io import *
from dotenv import load_dotenv


########--- Main variable definitions, should not change ---##########



MAINSERVER = "Dragonkind"
intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('&'),
    description = "Dragonkind is currently under development (v1.0.8).",
    activity = discord.Game(name=f"&help | Ready"),
    status = discord.Status.online,
    intents = intents
)
prefix = bot.command_prefix
finnhubKey = "c8jqh02ad3i8fk1jtkmg"
finnhubSandboxKey = "sandbox_c8jqh02ad3i8fk1jtkn0"# Change only if you get a new API key.
helpOn = False
financeOn = False

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#####################---- Status class def ----##########################
class Status:
    def __init__(self, status):
        self.status = status

    def new(self, status):
        self.status = status

    def main(self):
        self.status = "Ready"

stat = Status("Ready")
#####################---- DO NOT CHANGE ANYTHING ----####################

#Do not change!
@bot.event
async def on_ready():
    servers = bot.guilds
    print(f"Connected as {bot.user}")
    
#Do not change!
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('&'):
        if stat.status == "Ready":
            await bot.process_commands(message)
        else:
            await message.channel.send(f"Busy, try again in a second. Task: {stat.status}")




################---- Commands ----#############



# Main command cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    #What's new command
    @commands.command()
    async def whatsnew(self, ctx):
        stat.new("Running whatsnew command")
        await ctx.send(f'''
    Current version of bot: V1.0.2
    What's new:
    Added the "&today <symbol>" command that allows you to get info about any stock.
    Removed the "&useFinanceApi" command because it didn't work at all.
    Removed the "&useHelp" command because it didn't work at all.
    Updated the "&getInfo" command (it now displays various user information).
    Added the "&join" command that allows the bot to join the voice channel you're connected to.
    Added the "&leave" command that allows the bot to leave the voice channel.
    General bug fixes.''')
        stat.main()

    @commands.command()
    async def getInfo(self, ctx, user: discord.Member):
        stat.new("Getting info about user.")
        accDate = user.created_at.timestamp()
        accDate = datetime.datetime.utcfromtimestamp(int(accDate)).strftime('%m/%d/%Y, %H:%M:%S')
        rolelist = [r.mention for r in user.roles if r != ctx.guild.default_role]
        roles = ", ".join(rolelist)
        await ctx.send(f'''
    Got info about {user.mention}
    Name: {user.name}
    Account creation date: {accDate}
    Roles: {roles}
    Status: {str(user.status)}''')
        stat.main()
    
class Finance(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    #Finance API
    @commands.command()
    @commands.has_role("financeUser")
    async def today(self, ctx, symbol="ORCL"):
        stat.new("Getting finance info.")
        useSandbox = True
        if useSandbox == True:
            url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={finnhubSandboxKey}"
        else:
            url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={finnhubKey}"
        response = requests.get(url)
        data = response.json()
        if data["d"] == "null":
            await ctx.send("Invalid symbol.")
            return
        elif "error" in data.keys():
            await ctx.send(f"{data['error']}")
            return
        else:
            await ctx.send(f'''
    Symbol: {symbol}
    Current price: {data['c']}
    Change in price: {data['d']}
    Change in percent: {data['dp']}
    Highest price of the day: {data['h']}
    Lowest price of the day: {data['l']}
    Open price of the day: {data['o']}
    Previous close price: {data['pc']}
    ''')
        stat.main()

class Voice(commands.Cog):
    def __init__(self, bot: commands.Cog):
        self.bot = bot
    @commands.command()
    async def join(self, ctx):
        stat.new("Joining voice channel.")
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f"Joined channel {channel.name} ({channel.id})")
        except discord.ext.commands.errors.CommandInvokeError:
            ctx.send("You are not connected to a voice channel.")
            return
        stat.main()

    @commands.command()
    async def leave(self, ctx):
        stat.new("Leaving voice channel.")
        if(ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send(f"Left the channel.")
        else:
            await ctx.send("Not connected to a voice channel.")
        stat.main()

# Fun cog
class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Say command
    @commands.command()
    async def say(self, ctx, arg):
        stat.new("Saying something. Shh.")
        await ctx.send((arg+" ")*50)
        await ctx.send("Like you want to do that again.")
        stat.main()

    #Random command that makes the bot "super angry" (github.com/chillnchar/Dragonkind#doit)
    @commands.command()
    async def doit(self, ctx):
        stat.new("Insulting user.")
        await ctx.send(f"Lol, {ctx.author.mention} is dumb and a noob")
        stat.main()

class Development(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def addRole(self, ctx, user: discord.Member, role: discord.Role):
        stat.new("Adding roles.")
        await user.add_roles(role)
        stat.main()

    @commands.command()
    async def eval(self, ctx, e):
        stat.new("Evaluating code.")
        sys.stdout = buffer = StringIO()
        eval(e)
        await ctx.send(f"{buffer.getvalue()}")
        stat.main()

    @commands.command()
    async def ping(self, ctx):
        stat.new("Calculating latency.")
        await ctx.send(f"Latency: {bot.latency * 1000} ms")
        stat.main()

        

bot.add_cog(Main(bot))
bot.add_cog(Fun(bot))
bot.add_cog(Finance(bot))
bot.add_cog(Voice(bot))
bot.add_cog(Development(bot))
bot.run(token)
