import discord
from discord import channel
from discord.ext import commands

# client = discord.Client() # define the client
bot = commands.Bot(command_prefix='$') # this is the same functionality as defining the client in previous example

@bot.event
async def on_ready(): 
    print(f'We have logged in as {bot.user}')

channel_id = 887340724457197619 # this is the channel id for the workshop

"""
Like I said. There are many different ways to structure the code:
    1.	Use “on message” events
    2.	Using commands
    3.	Define your own functions
    4.	Use built in functions
"""

# 1. Use “on message” events. Saw this is previous example
"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$test'): # define the $test command
        await message.channel.send('Hello!')
"""

# 2. Using commands
@bot.command()
async def test2(ctx):
    await ctx.send('Hello!')

# 3. Define your own functions
@bot.command()
async def test3(ctx):
    channel_id = 885318664553918484
    channels = ctx.guild.channels # get every channel in the guild
    
    def get_channel():
        for idx, val in enumerate(channels):
            if val.id == channel_id:
                return channels[idx]
        return None
    
    voting = get_channel()
    await voting.send('Hello')

# 4. Use built in functions
@bot.command()
async def test4(ctx):
    channel_id = 885318664553918484
    voting = await bot.fetch_channel(channel_id)
    await voting.send('Hello')

# will get back to this if time allows
"""
@bot.command()
async def vote(ctx,*args):
    print(args)
"""

token = open('../token.txt', "r").read()
bot.run(token)
