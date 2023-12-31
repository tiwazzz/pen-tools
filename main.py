import os
import platform
import time
import discord
import cpuinfo
import ping3
import psutil
from discord.commands import Option
from discord.ext import tasks
from dotenv import load_dotenv

# functions created by everyone (Thanks everyone!)
import functions

# Load configuration file
load_dotenv()
token = os.getenv("BOT_TOKEN")
channelId = os.getenv('CHANNEL_ID')

# decare discord library
bot = discord.Bot()

# Showing on command-prompt
print("[ in ] Welcome to pen-tools project.")

# Prepared Variable
aboutCpuInfo = cpuinfo.get_cpu_info()
local_time = time.ctime(time.time())

# Event or something happend!
# Check Discord Ready?
@bot.event
async def on_ready():
    print(f"[ ok ] pen-tools project is running as {bot.user}")

# Automate Task (using channel id only!)
# Check CPU
@tasks.loop(seconds=2.0)
async def cpuChecker():
    try:
        cpuThreadUsage = psutil.cpu_percent(interval=1)
    except Exception as error:
        print(f"[ er ] Cannot get infomation, Error: {error}")
    return cpuThreadUsage

@cpuChecker.after_loop
async def afterCpuCheck():
    try:
        if float(cpuChecker) >= 80.00:
            message = f">>> **:warning:** CPU had using more 80 percents, Please check your server status now.\n**CPU Load:** {cpuChecker}%\n**Locate time:** {local_time}"
    except Exception as error:
        print(f"[ er ] Cannot sent message to Discord: {error}")
    await bot.get_channel(int(channelId)).send(message)

@tasks.loop(seconds=2.0)
async def ramChecker():
    try:
        ramUsedPercentage = psutil.virtual_memory().percent
    except Exception as error:
        print(f"[ er ] Cannot get infomation, Error: {error}")
    return ramUsedPercentage

@ramChecker.after_loop
async def afterRamCheck():
    try:
        if float(ramChecker) >= 70.00:
            print(f"[ wn ] RAM had been used 70 percents. RAM usage now : {ramChecker}% at {local_time}")
        elif float(ramChecker) >= 80.00:
            print(f"[ wn ] RAM had been used 80 percents. RAM usage now : {ramChecker}% at {local_time}")
            message = f">>> **:warning: RAM HAD BEEN USED OVER 80 PERCENTS :chart_with_upwards_trend: !!!**"
        else:
            print(f"[ ok ] RAM is enough for handle work load now. RAM usage now {ramChecker}% at {local_time}")
    except Exception as error:
        print(f"[ er ] Cannot sent message to Discord, Error: {error}")
    await bot.get_channel(channelId).send(message)

# Specification
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
        cpuAdsHz = "**:boom: libary not support**"
        cpuActHz = "**:boom: libary not support**"
        print(f"Error Message: {error}")
    await ctx.respond(f">>> **:information_source: Specification on CPU**\n:identification_card: Processor: {cpuName}, {cpuCore} cores/{cpuThreadCore} Threads\n:brain: Architecture: {cpuArch}\n:zap: Maximum clock speed: {cpuAdsHz}\n:zap: Actual clock speed: {cpuActHz}")

@bot.slash_command(description="Show about basic server's specification.")
async def about_server(ctx):
    hostname = platform.node()
    cpuName = aboutCpuInfo['brand_raw']
    cpuCore = psutil.cpu_count(logical=False)
    cpuThreadCore = psutil.cpu_count(logical=True)
    ramTotal = functions.byteToGb(psutil.virtual_memory().total)
    diskUsage = functions.byteToGb(psutil.disk_usage("/").used)
    diskTotal = functions.byteToGb(psutil.disk_usage("/").total)
    diskSpacePercent = psutil.disk_usage("/").percent
    try:
        cpuAdsHz = aboutCpuInfo['hz_advertised_friendly']
    except Exception as error:
        cpuAdsHz = "**:boom: libary not support**"
        print(f"Error Message: {error}")
    await ctx.respond(f">>> **:information_source: Specification on this server**\n:identification_card: Hostname: {hostname}\n:identification_card: Processor: {cpuName}, :brain: {cpuCore} cores/{cpuThreadCore} Threads x {cpuAdsHz}\n:pencil: RAM: {ramTotal} GB\n:floppy_disk: Disk: {diskUsage}/{diskTotal} GB, {diskSpacePercent} %")

# Status
@bot.slash_command(description="Show CPU status.")
async def status_cpu(ctx):
    cpuName = aboutCpuInfo['brand_raw']
    cpuCore = psutil.cpu_count(logical=False)
    cpuThreadCore = psutil.cpu_count(logical=True)
    cpuThreadUsage = psutil.cpu_percent(percpu=True)
    try:
        cpuAdsHz = aboutCpuInfo['hz_advertised_friendly']
    except Exception as error:
        cpuAdsHz = "**:boom: libary not support**"
        print(f"Error Message: {error}")
    await ctx.respond(f">>> **:information_source: CPU status on this server**\n:identification_card: Processor: {cpuName}, :brain: {cpuCore} cores/{cpuThreadCore} Threads x {cpuAdsHz}\n:brain::bar_chart: CPU usaged: {cpuThreadUsage}")

@bot.slash_command(description="Show RAM used on this server.")
async def staus_ram(ctx):
    ramTotal = functions.byteToGb(psutil.virtual_memory().total)
    ramUsed = functions.byteToGb(psutil.virtual_memory().used)
    ramFree = functions.byteToGb(psutil.virtual_memory().free)
    ramUsedPercentage = psutil.virtual_memory().percent
    await ctx.respond(f">>> **:information_source: RAM used on this server**\n:pencil: RAM total: {ramTotal} GB\n:pencil: RAM status: {ramUsed} GB/ {ramTotal} GB, {ramUsedPercentage}%\n:pencil:RAM free space: {ramFree} GB")

# Networking
@bot.slash_command(description="Show network adapters.")
async def about_inet(ctx):
    try:
        inetInfo = psutil.net_if_addrs()
        print(inetInfo.keys())
    except Exception as error:
        inetInfo = "**:boom: libary not support**"
        print(f"Error Message: {error}")
    await ctx.respond(f">>> **:information_source: Network interface on this server**\nInterfaces: {inetInfo.keys()}")

@bot.slash_command(iphynet="", description="Show detail about network interface on your select.")
async def detail_inet(ctx, iphynet: Option(str, "Please enter your interface example (en0): ", required = True, default = "")):
    await ctx.respond(f">>> **:earth_americas: {iphynet} adapter detail**\n")

@bot.slash_command(ip_des="", description="Check network or host destination on this server")
async def ping(ctx, ip_des: Option(str, "Please enter your IP destination (default: 1.1.1.1): ", required = False, default = "1.1.1.1")):
    try:
        pingRes = ping3.verbose_ping(ip_des, count=5)
        if pingRes == None:
            pingRes = f":white_check_mark: Connection normally at {ip_des}."
    except Exception as error:
        pingRes = f":boom: Connection had problem: {error}."
    await ctx.respond(f">>> **:information_source: Result from {ip_des}**\n:pencil:: {pingRes}")

@bot.slash_command(description="Thank you to using our project.")
async def about_bot(ctx):
    await ctx.respond(">>> We're com-sci students in Thailand :flag_th::computer:.\nThank you for using our project and comments for imporved our project too.\nAnd follow along with our project at GitHub this link: 'https://github.com/tiwazzz/'")

# Start Services
cpuChecker.start()
bot.run(token)
