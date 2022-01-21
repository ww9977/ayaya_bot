from distutils import extension
import discord
from discord.ext import commands
from core.classes import Cog_Ext
import json,datetime,asyncio,os

with open('settings.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print("[Bot online]")

for file in os.listdir('./cmds'):
    if file.endswith('.py'):
        name = file[:-3]
        bot.load_extension(f'cmds.{name}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])