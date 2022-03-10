# Privacy Policy
We DON'T save information about users- in variables OR online. All information collected (mainly user's username/discriminators) is dumped immediantly. See for yourself:

#### Server command to get username/roles of discord.User
```
@bot.command()
@commands.has_role("dev")
async def hackem(ctx, user: discord.User):
    await ctx.send(f"Getting info about {user.mention}...")
    roleList = [r.mention for r in user.roles if r != ctx.guild.default_role]
    roles = ", ".join(roleList)
    await ctx.send(f'''
Got information about {user.mention}:
Username: {user.name}
Roles: {roles}''')
```
#### DM command to get username/discriminator of message.author
```
@bot.command()
async def dmInfo(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send(f'''
Got information about {ctx.author.mention}:
Username: {ctx.author.name}''')
```
This information is dumped immediantly after usage.
