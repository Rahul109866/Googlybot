import os 
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('We have logged in as user {0.user}'.format(client))
    
client.run(TOKEN)