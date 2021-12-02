# Discord Bot Workshop Day02
Please review the Discord API [Terms of Service](https://discord.com/developers/docs/policy).
## Setup
- Create a new folder on your computer
- Your directory should look like this:
    ```
    my_directory/
    |
    ├── my_code/
    |   ├── cogs/
    |   |   ├── example.py
    |   ├── main.py
    |
    ├── token.txt
    ```
- Here is what mine looks like:
    - `main.py` and the `cogs` folder (with `example.py` inside) go within `my_code` folder
    <p align="center">
    <img src="../Extra Files/img1.png" alt="drawing" width="300"/>
    </p>
- If you use github, only push the `my_code` folder. Do not share your token.txt file anywhere or it will be reset
## Code
`main.py`
```python
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)

file_dir = './cogs'
for filename in os.listdir(file_dir):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

token = open('../token.txt', "r").read()
bot.run(token)
```
`example.py`
```python
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
    async def say(self, ctx, *, thing_to_say):
        """Use this section to explain what the command does"""
        await ctx.message.delete()
        await ctx.send(f'{thing_to_say}')

def setup(bot):
    bot.add_cog(Example(bot))
```
## Today's Goals:
- learn the general structure of `cogs` and `commands`
- work a few general examples
## Next Weeks Goals:
- Discuss how to host the bot on a server. 