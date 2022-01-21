import discord
from discord.ext import commands
from core.classes import Cog_Ext
import json

with open('settings.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class re_text(Cog_Ext):
    @commands.Cog.listener()
    async def re_msg(self, msg):
        if msg.content == "幹你娘":
            await msg.channel.send("0")


def setup(bot):
    bot.add_cog(re_text(bot))
