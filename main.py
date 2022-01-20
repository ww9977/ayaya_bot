import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("[Bot online]")

bot.run('OTMzMzQ3NDcxNTMzNDI4Nzg2.YegNkQ.QZgWVq5dHzUPr3VHDOcchA07DaI')
