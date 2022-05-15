from discord.ext import commands
import discord
import json
import requests

def space_clean(str):
        endword = ''
        index = 0
        for char in str:
            if char == ' ':
                endword = endword + '-'
            elif char == "'":
                if str[index + 1] != ' ':
                    endword = endword + '-'
            else:
                endword = endword + char
            index += 1
        return endword

class Weapons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="weapon")
    async def weapon(self, ctx: commands.Context, *, arg):
        arg = space_clean(arg)
        if arg == 'prototype-amber':
            response = requests.get('https://api.genshin.dev/weapons/amber-catalyst')
        elif arg == 'prototype-starglitter':
            response = requests.get('https://api.genshin.dev/weapons/prototype-grudge')
        else:
            response = requests.get('https://api.genshin.dev/weapons/' + arg)
        data = response.text
        JSONData = json.loads(data)
        
        if arg == 'prototype-amber':
            embed = discord.Embed(title='Prototype Amber')
        if arg == 'prototype-starglitter':
            embed = discord.Embed(title='Prototype Starglitter')
        embed.set_thumbnail(url="https://raw.githubusercontent.com/Marius-Toader/Kamisato-Bot/dev/assets/" + arg + ".png")
        embed.add_field(name="Passive name: " + JSONData['passiveName'], value=JSONData['passiveDesc'], inline=False)
        embed.add_field(name="Type", value=JSONData['type'], inline=True)
        embed.add_field(name="Rarity", value=str(JSONData['rarity']) + " ★", inline=True)
        embed.add_field(name="Base Attack", value=JSONData['baseAttack'], inline=True)
        embed.add_field(name="Second Stat", value=JSONData['subStat'], inline=True)
        await ctx.send(embed=embed)
        
    @weapon.error
    async def weapon_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.CommandInvokeError):
            await ctx.send("The `%weapon` command needs a certain weapon name to function properly (example: `%weapon rust`).\n")

def setup(bot):
    bot.add_cog(Weapons(bot))
    