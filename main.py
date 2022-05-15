from discord.ext import commands
from config import token
import discord

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "%", intents=intents)

bot.load_extension("hello")
bot.load_extension("cogs.music.music")
bot.load_extension("cogs.characters.characters")
bot.load_extension("cogs.weapons.weapons")

bot.run(token)
