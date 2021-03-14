import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if '#ミスチル' or '#Mr.Children' in message.content and message.content.startswith('#'):
        if 'ロード・アイ・ミス・ユー' in message.content:
            await message.channel.send(


client.run(token)
