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
    async def shame(self, ctx, *, reason):
        """Use this section to explain what the command does"""
        await ctx.message.delete()
        await ctx.send(f'shame on {reason}')

def setup(bot):
    bot.add_cog(Example(bot))
