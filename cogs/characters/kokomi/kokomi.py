import discord

async def kokomi_build(ctx):
    embed = discord.Embed(title='Build(s) for Sangonomiya Kokomi')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Nereid\'s Ascension*\n' +
                    '2. Elemental Skill - *Kurage\'s Oath*\n' +
                    '3. Normal Attack - *The Shape of Water*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Ocean-Hued Clam\n' +
                    'Tenacity of the Millelith', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: HP%/Energy Recharge%\n' +
                    '- For Goblet of Eonothem: Hydro DMG Bonus%\n' +
                    '- For Circlet of Logos: Healing Bonus%/HP%', inline=True)
    embed.add_field(name='Substats Priority', value='HP% > Energy Recharge% > ATK% > Elemental Mastery', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Everlasting Moonglow__\n' +
                    '__Prototype Amber__\n' +
                    '__Hakushin Ring__\n' +
                    'Thrilling Tales of Dragon Slayers\n' +
                    '__Sacrificial Fragments__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def kokomi_team(ctx):
    embed = discord.Embed(title='Team(s) for Sangonomiya Kokomi')
    embed.add_field(name='Electro-charged Team', value='Team composition:\n' +
                    '1. Sangonomiya Kokomi\n' +
                    '2. Beidou\n' +
                    '3. Fischl\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Raiden Shogun__\n' +
                    '__Traveler__\n' +
                    '__Xingqiu__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Freeze Team', value='Team composition:\n' +
                    '1. Sangonomiya Kokomi\n' +
                    '2. Kamisato Ayaka/Ganyu\n' +
                    '3. Cryo character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Venti__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Traveler__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Vaporized Team', value='Team composition:\n' +
                    '1. Sangonomiya Kokomi\n' +
                    '2. Xiangling\n' +
                    '3. Bennett\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Traveler__\n' +
                    '__Xingqiu__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)