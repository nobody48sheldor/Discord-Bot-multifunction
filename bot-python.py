import discord
import os
from sys import platform
import js2py as jp

client = discord.Client()

os.chdir('.env')
with open('token.txt', 'r') as tok:
    token = tok.read()
os.chdir('..')

def run(link):
    os.chdir('github_folder')
    print(os.name)
    os.system('git clone {}'.format(link))
    if platform == 'linux' or platform == "linux2":
        print('del link linux')
    if os.name == 'win32':
        print('del link windows')
    os.chdir('..')


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
        link = msg.content.lstrip('£run')
        await msg.channel.send(link)
        run(link)

client.run(token)
