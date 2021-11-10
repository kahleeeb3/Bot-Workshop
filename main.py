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
token = open('../token.txt', "r").read()
client.run(token)
