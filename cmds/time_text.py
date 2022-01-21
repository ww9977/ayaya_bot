import discord
from discord.ext import commands
from core.classes import Cog_Ext
import json,asyncio,datetime

class time_text(Cog_Ext):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        async def FFXIV_remind():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(933926989298008134)
            while not self.bot.is_closed():
                await self.channel.send("running")
                await asyncio.sleep(3)
    
        self.bg_task=self.bot.loop.create_task(FFXIV_remind())

def setup(bot):
    bot.add_cog(time_text(bot))