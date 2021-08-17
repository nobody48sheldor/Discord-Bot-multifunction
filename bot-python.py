import discord
import os
from sys import platform
import js2py as jp
from io import StringIO
import sys
import the_code
import importlib

client = discord.Client()

os.chdir('.env')
with open('token.txt', 'r') as tok:
    token = tok.read()
os.chdir('..')

def run(code):
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    if platform == "win32":
        os.system('cls')
    with open("the_code.py", "w+") as codef:
        codef.write("from io import StringIO\nimport sys\nsys.stdout = buffer = StringIO()\n{}\ndef main():\n    return(buffer.getvalue())".format(code))
    importlib.reload(the_code)
    return(the_code.main())


@client.event
async def on_ready():
    print("letssss goooo")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith('£help'):
        await msg.channel.send('help pannel in working...')
    if msg.content.startswith('£hi'):
        await msg.channel.send('hi!')
    if msg.content.startswith('£github'):
        await msg.channel.send('https://github.com/nobody48sheldor/Discord-Bot-multifunction')
    if msg.content.startswith('£run'):
        code = msg.content.lstrip('£run ')
        await msg.channel.send(run(code))

client.run(token)
