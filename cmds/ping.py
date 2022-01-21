import discord
from discord.ext import commands
from core.classes import Cog_Ext


class ping(Cog_Ext):

    @commands.command()
    async def return_ping(self, ctx):
      await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

def setup(bot):
    bot.add_cog(ping(bot))
