# Discord Bot Workshop

### Required
- An I.D.E. such as [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/) installed on your PC
<hr>

## Create a Discord bot
- Visit the [Discord Developer Portal](https://discord.com/developers/)
- Click `Create Application`
- Under `Settings` select the `Bot` option
- Select `Add Bot` and the `Yes, do it!`
- Copy your `bot token` and paste it into a text file on your computer
- Go to `OAuth2`, select the `bot` scope, and select the `Permissions` you would like the bot to have. 
- Copy and paste the url into a web browser to invite the bot

<hr>

## Write some Code!
Please consult the documentation at https://discordpy.readthedocs.io/
### Installing API
- You can get the library directly from PyPI:
    ```
    python3 -m pip install -U discord.py
    ```
- If you are using Windows, then the following should be used instead:
    ```
    py -3 -m pip install -U discord.py
    ```
<hr>

## Example code 
```python
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        said = message.content
        if said == "Hello":
            channel = message.channel
            user = message.author
            await channel.send(f'{user} said {said}')

client = MyClient()
token = open('token.txt', "r").read()
client.run(token)
```
`main.py`