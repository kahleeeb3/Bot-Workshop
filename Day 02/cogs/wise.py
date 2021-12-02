import discord
from discord.ext import commands, tasks
import requests

jobs = {
        'JobName' : '21949'
        }

payload = {
    'username':'yourwabashusername',
    'password':'yourpassword',
    'login': 'Login',
    'logMeln':'1'
}

class TimeCard(commands.Cog):
    """Clock in and out of his WISE Job"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ci(self,ctx,jobname):
        """Clock in"""
        print(f'Attempting to clock into {jobname}')

        def check_job(name):
            if jobname in jobs:
                return True
            else:
                return False

        def clock_in(id,payload):
            s = requests.session()
            response = s.post('https://www.wabash.edu/timecard/login.cfm', data = payload)
            login = s.get(f'https://www.wabash.edu/timecard/home.cfm?login={jobs[jobname]}')
            s.close()

        # check if the Job is within "jobs"
        if check_job(jobname):
                clock_in(jobs[jobname],payload)
                await ctx.send(f'Clocked into {jobname}.')
        else:
            await ctx.send(f'{jobname} is not a real job')
            
    @commands.command()
    async def co(self,ctx,jobname):
        """Clock Out"""

        def check_job(name):
            if jobname in jobs:
                return True
            else:
                return False

        def clock_out(id,payload):
            s = requests.session()
            response = s.post('https://www.wabash.edu/timecard/login.cfm', data = payload)
            logout = s.get(f'https://www.wabash.edu/timecard/home.cfm?leave={jobs[jobname]}')
            s.close()        

        # check if the Job is within "jobs"
        if check_job(jobname):
                clock_out(jobs[jobname],payload)
                await ctx.send(f'Clocked out of {jobname}.')
        else:
            await ctx.send(f'{jobname} is not a real job')
def setup(bot):
    bot.add_cog(TimeCard(bot))