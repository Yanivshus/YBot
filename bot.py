import os
import random
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
print(TOKEN)
print(GUILD)

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    print(message.content)


client.run(TOKEN)