import os
import platform
import discord
import cpuinfo
import psutil
from dotenv import load_dotenv

# functions created by everyone (Thanks everyone!)
import functions

bot = discord.Bot()

# Showing on command-prompt
print("[ in ] Welcome to pen-tools project.")

# Prepared Variable
aboutCpuInfo = cpuinfo.get_cpu_info()

# Discord slash commands
@bot.event
async def on_ready():
    print(f"[ ok ] pen-tools project is running as {bot.user}")

@bot.slash_command(description="Show about server's cpu specification.")
async def about_cpu(ctx):
    cpuName = aboutCpuInfo['brand_raw']
    cpuAmountCore = aboutCpuInfo['count']
    cpuArch = aboutCpuInfo['arch']
    try:
        cpuAdsHz = functions.byteToGb(aboutCpuInfo['hz_advertised'])
        cpuActHz = functions.byteToGb(aboutCpuInfo['hz_actual'])
    except Exception as error:
        cpuAdsHz = ":warning: Unable to retrieve the clock speed of your CPU because some libraries are not supported"
        cpuActHz = ":warning: Unable to retrieve the clock speed of your CPU because some libraries are not supported"
        print(f"[ er ] about_server slash command got some error\nError detail: {error}")
    await ctx.respond(f">>> :identification_card: Processor: {cpuName}\n:brain: Amount of core: {cpuAmountCore}\n:brain: Architecture: {cpuArch}\n:zap: Maximum clock speed: {cpuAdsHz}\n:zap: Actual clock speed: {cpuActHz}")

@bot.slash_command(description="Show about basic server's specification.")
async def about_server(ctx):
    cpuName = aboutCpuInfo['brand_raw']
    cpuAmountCore = aboutCpuInfo['count']
    cpuArch = aboutCpuInfo['arch']
    try:
        cpuAdsHz = functions.byteToGb(aboutCpuInfo['hz_advertised'])
        cpuActHz = functions.byteToGb(aboutCpuInfo['hz_actual'])
    except Exception as error:
        cpuAdsHz = ":warning: Unable to retrieve the clock speed of your CPU because some libraries are not supported"
        cpuActHz = ":warning: Unable to retrieve the clock speed of your CPU because some libraries are not supported"
        print(f"[ er ] about_server slash command got some error\nError detail: {error}")
    await ctx.respond(f">>> :identification_card: Processor: {cpuName}\n:brain: Amount of core: {cpuAmountCore}\n:brain: Architecture: {cpuArch}\n:zap: Maximum clock speed: {cpuAdsHz}\n:zap: Actual clock speed: {cpuActHz}")

@bot.slash_command(description="About us!!!")
async def about_us(ctx):
    await ctx.respond("We're just com-sci student in Thailand :flag_th::computer:.\nThank you for using our project and comments for imporved our project too.\nAnd follow along with our project at GitHub this link: 'some link this here lol'")

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))