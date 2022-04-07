from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix = "%")

bot.load_extension("hello")
bot.load_extension("cogs.music.music")

bot.run(token)
