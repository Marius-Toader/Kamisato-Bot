from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix = "%")

@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

bot.run(token)
