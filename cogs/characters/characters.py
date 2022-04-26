from discord.ext import commands
import discord
import json
import requests

class Characters(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="character")
    async def character(self, ctx: commands.Context, arg):
            response = requests.get('https://api.genshin.dev/characters/' + arg)
            data = response.text
            JSONData = json.loads(data)
            
            embed = discord.Embed(title=JSONData["name"])
            embed.set_thumbnail(url="https://raw.githubusercontent.com/Marius-Toader/Kamisato-Bot/dev/assets/" + arg + ".jpg")
            embed.add_field(name="Description", value=JSONData["description"], inline=False)
            embed.add_field(name="Nation", value=JSONData["nation"], inline=True)
            embed.add_field(name="Vision", value=JSONData["vision"], inline=True)
            embed.add_field(name="Weapon", value=JSONData["weapon"], inline=True)
            embed.add_field(name="Affiliation", value=JSONData["affiliation"], inline=True)
            embed.add_field(name="Rarity", value=str(JSONData["rarity"]) + " ★", inline=True)
            embed.add_field(name="Constellation", value=JSONData["constellation"], inline=True)
            await ctx.send(embed=embed)
    
    @character.error
    async def character_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.CommandInvokeError):
            await ctx.send("The `%character` command needs a certain character name to function properly (example: `%character albedo`). \n" +
                        "There are certain characters with more than one word in their name (example: Hu Tao). " +
                        "Here are the words required for those characters:\n" +
                        "- For Arataki Itto: `arataki-itto`\n" +
                        "- For Kamisato Ayaka: `ayaka`\n" +
                        "- For Hu Tao: `hu-tao`\n" +
                        "- For Kaedehara Kazuha: `kazuha`\n" +
                        "- For Sangonomiya Kokomi: `kokomi`\n" +
                        "- For Raiden Shogun: `raiden`\n" +
                        "- For Kujou Sara: `sara`\n" +
                        "- For Traveler: `traveler-`[`anemo`/`electro`/`geo`]\n" +
                        "- For Yun Jin: `yun-jin`")
            
def setup(bot: commands.Bot):
    bot.add_cog(Characters(bot))
