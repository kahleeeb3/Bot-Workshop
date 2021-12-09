import discord
from discord.ext import commands, tasks
import modules.save as poop # takes save.py in modules folder and renames it poop

class Store(commands.Cog):
    """Gets the last deleted message"""

    def __init__(self, bot):
        self.bot = bot

    """
    @commands.Cog.listener()
    async def on_message(self, message):
        poop.test(self,message)

    @commands.command()
    async def snipe(self, ctx):
        await ctx.send(poop.read())
    """
    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()

    @tasks.loop(seconds= 1)
    async def check(self):
        #print("hello")
        channel = self.bot.get_channel(887340724457197619)
        await channel.send("Yall need to wake up")


def setup(bot):
    bot.add_cog(Store(bot))