import discord
import json

def test(self,message):
    #print("Nobody in the back of the room pays attention")
    user= message.author.name
    content = message.content
    #print(f'{user} said {content}')
    write(user,content)
    print(read())

def write(user,content):
    data = {f"{user}":f"{content}"}
    with open('data.json', 'w') as f:
        json.dump(data, f)

def read():
    a_file = open("data.json", "r")
    data = json.load(a_file)
    return data["Rippy"]
