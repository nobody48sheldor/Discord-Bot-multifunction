import discord
import os

client = discord.Client()

os.chdir('.env')
with open('token.txt', 'r') as tok:
    token = tok.read()
os.chdir('..')

@client.event
async def on_ready():
    print("letssss goooo")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith('£hi'):
        await msg.channel.send('hi!')
    if msg.content.startswith('£github'):
        await msg.channel.send('https://github.com/nobody48sheldor/Discord-Bot-multifunction')

client.run(token)
