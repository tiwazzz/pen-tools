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
    try:
        cpuAdsHz = aboutCpuInfo['hz_advertised_friendly']
        cpuActHz = aboutCpuInfo['hz_actual_friendly']
    except Exception as error:
        cpuAdsHz = "**:octagonal_sign: libary not support**"
        cpuActHz = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    await ctx.respond(f">>> **:information_source: Specification on CPU**\n:identification_card: Processor: {cpuName}, {cpuCore} cores/{cpuThreadCore} Threads\n:brain: Architecture: {cpuArch}\n:zap: Maximum clock speed: {cpuAdsHz}\n:zap: Actual clock speed: {cpuActHz}")

@bot.slash_command(description="Show about basic server's specification.")
async def about_server(ctx):
    cpuName = aboutCpuInfo['brand_raw']
    cpuCore = psutil.cpu_count(logical=False)
    cpuThreadCore = psutil.cpu_count(logical=True)
    ramTotal = functions.getRamTotal()
    diskUsage = functions.byteToGb(psutil.disk_usage("/").used)
    diskTotal = functions.byteToGb(psutil.disk_usage("/").total)
    diskSpacePercent = psutil.disk_usage("/").percent
    try:
        cpuAdsHz = aboutCpuInfo['hz_advertised_friendly']
    except Exception as error:
        cpuAdsHz = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    await ctx.respond(f">>> **:information_source: Specification on this server**\n:identification_card: Processor: {cpuName}, :brain: {cpuCore} cores/{cpuThreadCore} Threads x {cpuAdsHz}\n:pencil: RAM: {ramTotal} GB\n:floppy_disk: Disk: {diskUsage}/{diskTotal} GB, {diskSpacePercent} %")

@bot.slash_command(description="Show CPU status.")
async def status_cpu(ctx):
    
    await ctx.response(f"")

@bot.slash_command(description="Thank you to using our project.")
async def thank_you(ctx):
    await ctx.respond(">>> We're com-sci students in Thailand :flag_th::computer:.\nThank you for using our project and comments for imporved our project too.\nAnd follow along with our project at GitHub this link: 'some link this here lol'")

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))