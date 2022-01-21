import discord
from discord.ext import commands
from core.classes import Cog_Ext


class net_comd(Cog_Ext):
    @commands.command()
    async def ping(self, ctx):
      await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

def setup(bot):
    bot.add_cog(net_comd(bot))
