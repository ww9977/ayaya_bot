import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,datetime,asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print("[Bot online]")

@bot.event
async def 


bot.run('OTMzMzQ3NDcxNTMzNDI4Nzg2.YegNkQ.QZgWVq5dHzUPr3VHDOcchA07DaI')
