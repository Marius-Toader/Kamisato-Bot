from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix = "%")

bot.load_extension("hello")

bot.run(token)
