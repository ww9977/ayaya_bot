from time import sleep
import discord
from discord.ext import commands
from core.classes import Cog_Ext
from datetime import datetime
import json,asyncio


class time_text(Cog_Ext):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        async def FFXIV_remind():
         await self.bot.wait_until_ready()
         while not self.bot.is_closed():
             if datetime.today().isoweekday() == 6:
                 self.channel=self.bot.get_channel(933926989298008134)
                 await self.channel.send('abyss')
             sleep(59)    
         
    
        self.bg_task=self.bot.loop.create_task(FFXIV_remind())
    

def setup(bot):
    bot.add_cog(time_text(bot))