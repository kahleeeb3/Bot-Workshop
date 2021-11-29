import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready(): 
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def test(ctx):
    channels = ctx.guild.channels # get every channel in the guild
    #ids = [x.id for x in channels] # get every id for the channel
    channel_id = 885318664553918484
    
    def get_channel():
        for idx, val in enumerate(channels):
            if val.id == channel_id:
                return channels[idx]
        return None
    #voting = get_channel()
    voting = await bot.fetch_channel(channel_id)
    await voting.send('Hello')
    

@bot.command()
async def vote(ctx,*args):
    print(args)

token = open('../token.txt', "r").read()
bot.run(token)
