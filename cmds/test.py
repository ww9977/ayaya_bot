import discord
from discord.ext import commands
from core.classes import Cog_Ext
import json,asyncio,datetime

class test(Cog_Ext):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

def setup(bot):
    bot.add_cog(test(bot))
