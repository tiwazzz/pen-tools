import os
import discord
import cpuinfo
import psutil
from dotenv import load_dotenv

# functions created by everyone (Thanks everyone!)
import functions

# decare discord library
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
    cpuArch = aboutCpuInfo['arch_string_raw']
    cpuCore = psutil.cpu_count(logical=False)
    cpuThreadCore = psutil.cpu_count(logical=True)
    cpuAdsHz = functions.getAdsClockSpeed()
    cpuActHz = functions.getActsClockSpeed()
    cpuL1cache = functions.getCpuL1()
    cpuL2cache = functions.getCpuL2()
    cpuL3cache = functions.getCpuL3()
    await ctx.respond(f">>> **:information_source: Specification on CPU**\n:identification_card: Processor: {cpuName}, {cpuCore} cores/{cpuThreadCore} Threads\n:brain: Architecture: {cpuArch}\n:zap: Maximum clock speed: {cpuAdsHz}\n:zap: Actual clock speed: {cpuActHz}\n:inbox_tray: L1 Cache: {cpuL1cache}\n:inbox_tray: L2 Cache: {cpuL2cache}\n:inbox_tray: L3 Cache: {cpuL3cache}\n")

@bot.slash_command(description="Show about basic server's specification.")
async def about_server(ctx):
    cpuName = aboutCpuInfo['brand_raw']
    cpuAmountCore = aboutCpuInfo['count']
    cpuAdsHz = functions.getAdsClockSpeed()
    ramTotal = functions.getRamTotal()
    diskUsage = "empty"
    diskTotal = "empty"
    await ctx.respond(f">>> **:information_source: Specification on this server**\n:identification_card: Processor: {cpuName}, :brain: {cpuAmountCore} core x {cpuAdsHz} GHz\n:pencil: RAM: {ramTotal} GB\n:floppy_disk: Disk: {diskUsage}/{diskTotal} GB")

@bot.slash_command(description="Thank you to using our project.")
async def thank_you(ctx):
    await ctx.respond(">>> We're com-sci students in Thailand :flag_th::computer:.\nThank you for using our project and comments for imporved our project too.\nAnd follow along with our project at GitHub this link: 'some link this here lol'")

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))