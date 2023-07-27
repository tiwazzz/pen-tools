import os
import platform
import discord
from dotenv import load_dotenv

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))