import discord
from discord.ext.commands import Bot
import os

BOT_PREFIX = "!"
BOT_TOKEN = os.environ.get('YOUTUBE_BOT_TOKEN')

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    """This function runs when the bot is started
    """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    author = message.author.display_name
    print(author)
    await client.process_commands(message)

@client.command(name='r') #!r
async def respond(ctx):
    await ctx.send("Hello " + ctx.author.display_name)

client.run(BOT_TOKEN)