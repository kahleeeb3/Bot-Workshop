import discord
from discord.ext import commands

class Example(commands.Cog):
    """Its good practice to explain the use case of the class here"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')
    
    @commands.command()
    async def say(self, ctx, *, thing_to_say): # "thing_to_say" is everything after the command
        """Use this section to explain what the command does"""
        await ctx.message.delete() # Deletes message
        await ctx.send(f'{thing_to_say}') # send the reason is the chat

    @commands.command()
    async def test(self, ctx, *args):
        print(args)

def setup(bot):
    bot.add_cog(Example(bot))
