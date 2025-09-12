import discord, datetime, requests, sys
from discord.ext import commands
from io import *

finnhubKey = "c8jqh02ad3i8fk1jtkmg"
finnhubSandboxKey = "sandbox_c8jqh02ad3i8fk1jtkn0"

# Main command cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    #What's new command
    @commands.command()
    async def whatsnew(self, ctx):
        """
Gets the release notes."""
        await ctx.send(f'''
    Current version of bot: V1.0.2
    What's new:
    Added the "&ping" command to get the latency of the bot.
    Added the "&addRole" command to add roles.
    Added the "&eval" command to execute Python code.
    If you run a command at the same time as someone else, it will give a new
    message saying it is busy.
    General bug fixes.''')

    @commands.command()
    async def getInfo(self, ctx, user: discord.Member):
        """Gets info of user."""
        accDate = user.created_at.timestamp()
        accDate = datetime.datetime.utcfromtimestamp(int(accDate)).strftime('%m/%d/%Y, %H:%M:%S')
        rolelist = [r.mention for r in user.roles if r != ctx.guild.default_role]
        roles = ", ".join(rolelist)
        await ctx.send(f'''
    Got info about {user.mention}
    Name: {user.name}
    Account creation date: {accDate}
    Roles: {roles}
    Status: {user.raw_status}''')
    
class Finance(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    #Finance API
    @commands.command()
    @commands.has_role("financeUser")
    async def today(self, ctx, symbol="ORCL"):
        """Gets finance info."""
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

class Voice(commands.Cog):
    def __init__(self, bot: commands.Cog):
        self.bot = bot
    @commands.command()
    async def join(self, ctx):
        """Joins a voice channel."""
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f"Joined channel {channel.name} ({channel.id})")
        except discord.ext.commands.errors.CommandInvokeError:
            ctx.send("You are not connected to a voice channel.")
            return

    @commands.command()
    async def leave(self, ctx):
        """Leaves a voice channel."""
        if(ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send(f"Left the channel.")
        else:
            await ctx.send("Not connected to a voice channel.")
        

# Fun cog
class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Say command
    @commands.command()
    async def say(self, ctx, arg):
        """Repeats text over and over."""
        await ctx.send((arg+" ")*50)
        await ctx.send("Like you want to do that again.")

    #Random command that makes the bot "super angry" (github.com/chillnchar/Dragonkind#doit)
    @commands.command()
    async def doit(self, ctx):
        """Random."""
        await ctx.send(f"Lol, {ctx.author.mention} is dumb and a noob")

class New(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def addRole(self, ctx, user: discord.Member, role: discord.Role):
        """Adds a role."""
        await user.add_roles(role)

    @commands.command()
    async def eval(self, ctx, e):
        """Evaluates a command."""
        sys.stdout = buffer = StringIO()
        eval(e)
        await ctx.send(f"{buffer.getvalue()}")

    @commands.command()
    async def ping(self, ctx):
        """Gets latency of the bot."""
        await ctx.send(f"Latency: {self.bot.latency * 1000} ms")

class Development(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def fire(self, ctx, user: discord.Member, reason: str=None):
        """Kicks a member."""
        await user.kick(reason=reason)
        await ctx.send(f"Member kicked for {reason}.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def greekFire(self, ctx, user: discord.Member, reason: str):
        """Bans a member."""
        await user.ban(reason=reason)
        await ctx.send(f"Banned from server for {reason}.")

    @commands.command()
    async def embed(self, ctx, title: str="No title", url: str=None, des: str="No description", color: discord.Color=discord.Color.red()):
        """Makes an embed."""
        embed = discord.Embed(title=title, url=url, description=des, color=color)
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Main(bot))
    await bot.add_cog(Fun(bot))
    await bot.add_cog(Finance(bot))
    await bot.add_cog(Voice(bot))
    await bot.add_cog(New(bot))
    await bot.add_cog(Development(bot))
