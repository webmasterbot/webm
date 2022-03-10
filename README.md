# Dragonkind
This is the GitHub repository for the Dragonkind Discord bot. This robot is in development, so add to your server and twiddle your thumbs. <br>

##### Dragonkind is going to shift versions! V 1.0.2 is coming soon.
[Get the bot](https://discord.com/api/oauth2/authorize?client_id=908462997687660574&permissions=8&scope=bot)

# Commands
## &whatsnew
Returns the release notes of the bot's current version.

## &say `text`
Returns `text`. But beware! It could get a little repetitive... <br>
![say snirt](https://user-images.githubusercontent.com/71795010/156643439-8d07ef25-9e8b-4bdd-8a9c-42f1f26ce71c.png)

## &useHelp
Enables the help channel plugin. NOTE: This is dependent upon the plugin being present upon the host computer (running the `bot.py` program) and there being the proper categories:<br>
* Available channels
* Claimed channels
* plus the help channels themselves!

## &stopHelp
Stops the help channels plugin from running.

## &useFinanceApi
Enables the finance API plugin. NOTE: This is dependent upon the plugin being present upon the host computer (running the `bot.py` program).

## &stopFinanceApi
Stops the finance API plugin from running.

## &doit
Try this command and never use it again. This command makes the bot angry. 😡

## &dmInfo
Gets your information specifically.

# Dev commands
These require the role "dev" to be given.
## &hackem `user`
Gets information about `user`: username, discriminator and roles.
## &ping `site`
Uses "ping `site`" from Windows Command Prompt. This is a developer command due to the fact that it uses the host computer's Command Prompt, and these windows popping up can be quite annoying!

# User-specific commands
These commands can be used by one user and ONLY one user- the creator of this bot.

## sendAllServers `message`
This command is only used to send a message to all servers this robot is in, probably about the latest version released.
