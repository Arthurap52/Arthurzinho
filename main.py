import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", ".")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

WELCOME_CHANNEL = 772928022922920016

bot = commands.Bot(PREFIX, intents=intents)

@bot.event
async def on_ready():
    syncs = await bot.tree.sync()
    print(f"{len(syncs)} Comentados Sincronizados.")
    print(f"Bot online e logado como {bot.user}!")

@bot.event
async def on_member_join(member:discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL)
    await channel.send(f"{member.mention} entrou no servidor!")

async def load_extensions():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")

@bot.tree.command()
async def invite_link(interact:discord.Interaction):
    await interact.response.defer()
    await interact.followup.send("https://discord.gg/yBsJgcEc", ephemeral=True)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)
        await print("Bot started")

asyncio.run(main())
