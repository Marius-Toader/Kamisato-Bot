# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import json
import requests

characters_search_parameters = ['vision', 'weapon', 'nation', 'rarity']

weapons_search_parameters = ['type', 'rarity', 'baseAttack', 'subStat']

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="search")
    async def search(self, ctx: commands.Context, arg1, arg2, *, arg3):
        if arg1 == 'characters':
            if arg2 in characters_search_parameters:
                result = []
                values = ""
                response = requests.get('https://api.genshin.dev/characters/')
                data = response.text
                JSONData = json.loads(data)
                
                for character in JSONData:
                    response = requests.get('https://api.genshin.dev/characters/' + character)
                    data = response.text
                    JSONData = json.loads(data)
                    
                    if JSONData[arg2] == arg3:
                        result.append(JSONData["name"])
            else:
                text = "The only parameters allowed are "
                for parameter in characters_search_parameters:
                    text = text + '`' + parameter + '` '
                await ctx.send(text)
                        
            for entity in result:
                values = "- " + entity + "\n"
            
            embed = discord.Embed(title="Search result(s)")
            embed.add_field(name="Character(s) that match your search parameters:", value=values, inline=False)
            await ctx.send(embed=embed)
            
        elif arg1 == 'weapons':
            if arg2 in weapons_search_parameters:
                response = requests.get('https://api.genshin.dev/weapons/')
                data = response.text
                JSONData = json.loads(data)
                
                for weapon in JSONData:
                    response = requests.get('https://api.genshin.dev/weapons/' + weapon)
                    data = response.text
                    JSONData = json.loads(data)
                    
                    if JSONData[arg2] == arg3:
                        result.append(JSONData["name"])
            
            
            values = ""
            for value in result:
                values = "- " + value + "\n"
                
            embed = discord.Embed(title="Search result(s)")
            embed.add_field(name="Weapon(s) that match your search parameters:", value=values, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("The only arguments allowed to search are `characters` and `weapons`.")

def setup(bot):
    bot.add_cog(Search(bot))
