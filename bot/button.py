import discord, sys
from discord.ext import commands
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('&'),
    description = "Dragonkind is currently under development (v1.1.2).",
    activity = discord.Game(name=f"&help | Ready"),
    status = discord.Status.online,
    intents = discord.Intents.all()
)

class Button(discord.ui.View):
        def __init__(self, *, timeout=180):
            super().__init__(timeout=timeout)

        @discord.ui.button(label="Click me", style=discord.ButtonStyle.gray)
        async def btn(self, btn: discord.ui.Button, ini=discord.Interaction):
            await btn.response.edit_message(content="Whoa, you clik that buttonnn")

        @discord.ui.button(label="End Interaction", style=discord.ButtonStyle.primary)
        async def end(self, btn, ini):
                for child in self.children:
                        child.disabled=True
                await btn.response.edit_message(view=self)

class mainSettingsView(discord.ui.View):
        def __init__(self, *, tm=180):
                super().__init__(timeout=tm)

        @discord.ui.button(label="Stop Bot", style=discord.ButtonStyle.danger)
        async def stopEverything(self, btn, ini):
                for child in self.children:
                        child.disabled=True
                await btn.response.edit_message("Bot stopped.")
                sys.exit(1)

class ButtonsPlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getMeAButton(self, ctx):
        await ctx.send("Hey why don't you click this button?", view=Button())

class BotSettings(commands.Cog):
        def __init__(self, bot):
                self.bot=bot

        @commands.command()
        @commands.has_permissions(administrator=True)
        async def STOPALL(self, ctx):
                await ctx.send("Are you sure? Stopping the bot will reset everything.", view=mainSettingsView())


async def setup(bot):
    await bot.add_cog(ButtonsPlay(bot))
    await bot.add_cog(BotSettings(bot))
