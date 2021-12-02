import discord
from discord.ext import commands
import os

ints = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', Intents=ints)

file_dir = './cogs'
for filename in os.listdir(file_dir):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

token = open("../../token.txt", "r").read()
bot.run(token)