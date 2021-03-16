import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if '#Mr.Children:' in message.content and message.content.startswith('#Mr.Children:'):
        kasi = message.content.replace('#Mr.Children:', '')
        with open(kasi) as kasii:
            kasiyaru = kasii.read()
        await message.channel.send(kasiyaru)
                 
                 
      


client.run(token)
