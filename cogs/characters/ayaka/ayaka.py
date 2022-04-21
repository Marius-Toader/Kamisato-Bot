from discord.ext import commands
import discord
import json
import requests

class Ayaka(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="ayaka")
    async def ayaka(self, ctx: commands.Context):
        response = requests.get('https://api.genshin.dev/characters/ayaka')
        data = response.text
        JSONData = json.loads(data)
        
        embed = discord.Embed(title=JSONData["name"])
        embed.set_thumbnail(url="https://raw.githubusercontent.com/Marius-Toader/Kamisato-Bot/dev/assets/ayaka.jpg")
        embed.add_field(name="Description", value=JSONData["description"], inline=False)
        embed.add_field(name="Nation", value=JSONData["nation"], inline=True)
        embed.add_field(name="Vision", value=JSONData["vision"], inline=True)
        embed.add_field(name="Weapon", value=JSONData["weapon"], inline=True)
        embed.add_field(name="Affiliation", value=JSONData["affiliation"], inline=True)
        embed.add_field(name="Rarity", value=str(JSONData["rarity"]) + " ★", inline=True)
        embed.add_field(name="Constellation", value=JSONData["constellation"], inline=True)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Ayaka(bot))
