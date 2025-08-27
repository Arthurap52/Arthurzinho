import discord
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx:commands.Context):
        await ctx.send(f"Ping! Latência: {round(self.bot.latency * 1000)}ms")

    @commands.command(name="hello")
    async def hello(self, ctx:commands.Context):
        author = ctx.author.mention
        await ctx.send(f"Olá {author}, eu sou o Arthurzinho 🤖")

async def setup(bot):
    await bot.add_cog(Core(bot))
