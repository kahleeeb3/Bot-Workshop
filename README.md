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

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

token = open('token.txt', "r").read()
client.run(token)
```
`main.py`