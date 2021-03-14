import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

with open('kasi.txt') as f:
    kasi_dict = {line.split(':')[0]: line[1] for line in f.readlines()}

@client.event
async def on_message(message):
    if '#ミスチル' or '#Mr.Children' in message.content and message.content.startswith('#'):
        kasi_str = message.content
        kasi_str.remove('#ミスチル' or '#Mr.Children')
        kasi = kasi_str
        await message.channel.send(kasi_dict[kasi])
                 
                 
      


client.run(token)
