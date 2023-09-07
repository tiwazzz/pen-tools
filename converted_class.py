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

class DisCommands:
    def __init__(self) -> None:
        