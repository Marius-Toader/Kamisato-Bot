import discord

async def eula_build(ctx):
    embed = discord.Embed(title='Build(s) for Eula')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Glacial Illumination*\n' +
                    '2. Normal Attack - *Favonius Bladework - Edel*\n' +
                    '3. Elemental Skill - *Icetide Vortex*', inline=False)
    embed.add_field(name='Artifact Set', value= 
                    'Pale Flame', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%\n' +
                    '- For Goblet of Eonothem: Physical DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% >= Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Song of Broken Pines__\n' +
                    '__Wolf\'s Gravestone__\n' +
                    '__The Unforged__\n' +
                    '__Skyward Pride__\n' +
                    '__Serpent\'s Spine__\n' +
                    '__Luxurious Sea-Lord__\n' +
                    '__Snow-Tombed Starsilver__\n' +
                    '__Akuoumaru__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def eula_team(ctx):
    embed = discord.Embed(title='Team(s) for Eula')
    embed.add_field(name='Superconduct Team', value='Team composition:\n' +
                    '1. Eula\n' +
                    '2. Electro character\n' +
                    '3. Cryo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Fischl__\n' +
                    '__Beidou__\n' +
                    '__Raiden Shogun__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Bennett__\n' + 
                    '__Zhongli__\n' +
                    '__Albedo__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Double Geo Team', value='Team composition:\n' +
                    '1. Eula\n' +
                    '2. Cryo character\n' +
                    '3. Zhongli\n' +
                    '4. Albedo', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Mono Cryo Team', value='Team composition:\n' +
                    '1. Eula\n' +
                    '2. Cryo character\n' +
                    '3. Cryo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Zhongli__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)