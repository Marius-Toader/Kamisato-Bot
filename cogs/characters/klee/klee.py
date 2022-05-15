import discord

async def klee_build(ctx):
    embed = discord.Embed(title='Build(s) for Klee')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Kaboom!*\n' +
                    '2. Elemental Skill - *Jumpy Dumpty*\n' +
                    '3. Elemental Burst - *Sparks \'n\' Splash*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Crimson Witch of Flames/+18 ATK%\n' +
                    'Crimson Witch of Flames\n' +
                    'Lavawalker', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%/Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Pyro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > Energy Recharge% > ATK% >= Elemental Mastery%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__The Widsith__\n' +
                    '__Dodoco Tales__\n' +
                    '__Lost Prayer to the Sacred Winds__\n' +
                    '__Skyward Atlas__\n' +
                    '__Solar Pearl__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def klee_team(ctx):
    embed = discord.Embed(title='Team(s) for Klee')
    embed.add_field(name='Mono Pyro Team', value='Team composition:\n' +
                    '1. Klee\n' +
                    '2. Bennett\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Xiangling__\n' +
                    '__Zhongli__\n', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Vaporized Team', value='Team composition:\n' +
                    '1. Klee\n' +
                    '2. Bennett\n' +
                    '3. Hydro character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Xingqiu__\n' +
                    '__Mona__\n' +
                    '__Xiangling__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Sucrose__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Melt Team', value='Team composition:\n' +
                    '1. Klee\n' +
                    '2. Pyro character\n' +
                    '3. Cryo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Sucrose__\n' +
                    '__Bennett__\n' +
                    '__Xiangling__\n' +
                    '__Rosaria__\n' +
                    '__Diona__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)