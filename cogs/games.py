import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="jokenpo")
    async def jokenpo(self, ctx:commands.Context, user_choice: str):
        choices = ["pedra", "papel", "tesoura"]
        bot_choice = random.choice(choices)

        if user_choice not in choices:
            return await ctx.send("Use: `.jokenpo pedra|papel|tesoura`")

        if user_choice == bot_choice:
            result = "Empate!"
        elif (user_choice == "pedra" and bot_choice == "tesoura") or \
             (user_choice == "papel" and bot_choice == "pedra") or \
             (user_choice == "tesoura" and bot_choice == "papel"):
            result = "Você ganhou! 🎉"
        else:
            result = "Você perdeu! 😢"

        await ctx.reply(f"Você escolheu **{user_choice}**\nArthurzinho escolheu **{bot_choice}**\n➡ {result}")

async def setup(bot):
    await bot.add_cog(Games(bot))
