# Dragonkind
This is the GitHub repository for the Dragonkind Discord bot. <br>

##### Dragonkind v1.0.8 will launch on April 8th.

##### We'd appreciate your feedback! <a href="https://forms.gle/jpRsdyQzcKaJtApm8">Submit feedback</a>

# Links to pages not included
<a href="https://dragonkind-discord.github.io/dragonkind/SECURITY"><button>Security</button></a><br>
<a href="https://dragonkind-discord.github.io/dragonkind/privacy"><button>Privacy Policy</button></a>

# Command updates
There have been a few changes to commands:
* The commands are now in classes (commands.Cog) to allow for organization
* New command addRole allows you to add roles to users (required: discord.Member, discord.Role)
* New command eval allows you to execute Python code through the bot
* Introducing "Status", tells you whether the bot is currently executing a command (in beta testing, will go live in v1.1.0)
* New command ping tells you how slow the bot responds to commands.

# Commands
## &whatsnew
Returns the release notes of the bot's current version.

## &say `text`
Returns `text`. But beware! It could get a little repetitive... <br>
![say snirt](https://user-images.githubusercontent.com/71795010/156643439-8d07ef25-9e8b-4bdd-8a9c-42f1f26ce71c.png)

## &doit
Try this command and never use it again. This command makes the bot a little frustrated. Lol.

## &getInfo `user`
Gets information about `user`: username, account creation date, and roles. This command is now open to all users.

## &join
If you are connected to a voice channel, the bot will connect to it.

## &leave
Leaves the voice channel.

## &addRole `discord.Member` `discord.Role`
When you mention a user and role, it adds the role to the user.

## &ping
Gets the latency.

## &eval `e`
Executes `e`. e must be Python code.
