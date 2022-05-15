from .albedo.albedo import *
from .aloy.aloy import *
from .ayaka.ayaka import *
from .diluc.diluc import *
from .eula.eula import *
from .ganyu.ganyu import *
from .hutao.hutao import *
from .kazuha.kazuha import *
from .keqing.keqing import *
from .klee.klee import *
from .kokomi.kokomi import *
from .mona.mona import *
from .raiden.raiden import *
from .tartaglia.tartaglia import *
from .venti.venti import *
from .xiao.xiao import *
from .yoimiya.yoimiya import *
from .zhongli.zhongli import *
from discord.ext import commands
import discord
import json
import requests

class Characters(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="character")
    async def character(self, ctx: commands.Context, arg, arg2):
        if arg2 is None:    
            response = requests.get('https://api.genshin.dev/characters/' + arg)
            data = response.text
            JSONData = json.loads(data)
            
            embed = discord.Embed(title=JSONData["name"])
            embed.set_thumbnail(url="https://raw.githubusercontent.com/Marius-Toader/Kamisato-Bot/dev/assets/" + arg + ".jpg")
            embed.add_field(name="Description", value=JSONData["description"], inline=False)
            embed.add_field(name="Nation", value=JSONData["nation"], inline=True)
            if arg == 'venti' or arg == 'zhongli' or arg == 'raiden':
                embed.add_field(name="Gnosis", value=JSONData["vision"], inline=True)
            else:
                embed.add_field(name="Vision", value=JSONData["vision"], inline=True)
            embed.add_field(name="Weapon", value=JSONData["weapon"], inline=True)
            embed.add_field(name="Affiliation", value=JSONData["affiliation"], inline=True)
            embed.add_field(name="Rarity", value=str(JSONData["rarity"]) + " ★", inline=True)
            embed.add_field(name="Constellation", value=JSONData["constellation"], inline=True)
            await ctx.send(embed=embed)
        
        else:
            if arg2 == 'build':
                if arg == 'ayaka':
                    await ayaka_build(ctx)
                elif arg == 'hu-tao':
                    await hutao_build(ctx)
                elif arg == 'raiden':
                    await raiden_build(ctx)
                elif arg == 'kazuha':
                    await kazuha_build(ctx)
                elif arg == 'eula':
                    await eula_build(ctx)
                elif arg == 'xiao':
                    await xiao_build(ctx)
                elif arg == 'zhongli':
                    await zhongli_build(ctx)
                elif arg == 'ganyu':
                    await ganyu_build(ctx)
                elif arg == 'aloy':
                    await aloy_build(ctx)
                elif arg == 'albedo':
                    await albedo_build(ctx)
                elif arg == 'tartaglia':
                    await tartaglia_build(ctx)
                elif arg == 'yoimiya':
                    await yoimiya_build(ctx)
                elif arg == 'venti':
                    await venti_build(ctx)
                elif arg == 'kokomi':
                    await kokomi_build(ctx)
                elif arg == 'diluc':
                    await diluc_build(ctx)
                elif arg == 'keqing':
                    await keqing_build(ctx)
                elif arg == 'klee':
                    await klee_build(ctx)
                elif arg == 'mona':
                    await mona_build(ctx)
                
            elif arg2 == 'team':
                if arg == 'ayaka':
                    await ayaka_team(ctx)
                elif arg == 'hu-tao':
                    await hutao_team(ctx)
                elif arg == 'raiden':
                    await raiden_team(ctx)
                elif arg == 'kazuha':
                    await kazuha_team(ctx)
                elif arg == 'eula':
                    await eula_team(ctx)
                elif arg == 'xiao':
                    await xiao_team(ctx)
                elif arg == 'zhongli':
                    await zhongli_team(ctx)
                elif arg == 'ganyu':
                    await ganyu_team(ctx)
                elif arg == 'aloy':
                    await aloy_team(ctx)
                elif arg == 'albedo':
                    await albedo_team(ctx)
                elif arg == 'tartaglia':
                    await tartaglia_team(ctx)
                elif arg == 'yoimiya':
                    await yoimiya_team(ctx)
                elif arg == 'venti':
                    await venti_team(ctx)
                elif arg == 'kokomi':
                    await kokomi_team(ctx)
                elif arg == 'diluc':
                    await diluc_team(ctx)
                elif arg == 'keqing':
                    await keqing_team(ctx)
                elif arg == 'klee':
                    await klee_team(ctx)
                elif arg == 'mona':
                    await mona_team(ctx)
            else:
                await ctx.send('The only 2 parameters allowed in the 2nd slot are `build` and `team`.')
    
    """@character.error
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
                        "- For Yun Jin: `yun-jin`")"""
            
def setup(bot: commands.Bot):
    bot.add_cog(Characters(bot))
