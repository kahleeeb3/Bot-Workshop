import discord

client = discord.Client() # define the client

@client.event # event decorator that registers an event
async def on_ready(): 
    # discord.py is an asynchronous library => everything is done in callbacks i.e. (async def)
    # a callback is a function that is called when somehing else happens i.e. "on ready"
    print(f'We have logged in as {client.user}')
    #print('We have logged in as {0.user}'.format(client)) # does the same thing

@client.event
async def on_message(message): # discord.py looks for these function names when stuff happens
    if message.author == client.user: # if the message is sent by the bot
        return

    if message.content.startswith('$hello'): 
        await message.channel.send('Hello!')

token = open('../token.txt', "r").read()
client.run(token)
