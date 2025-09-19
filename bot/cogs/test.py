import discord
from discord.ext import commands
from discord import app_commands

class Test(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@app_commands.command(name="test", description="Summarizes working services")
	async def test(self, interaction: discord.Interaction):
		await interaction.response.send("Tested and working, tried and true :D")

	async def cog_load(self):
		self.bot.tree.add_command(self.test)

async def setup(bot: commands.Bot):
	bot.add_cog(Test(bot))
