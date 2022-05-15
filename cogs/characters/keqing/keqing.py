import discord

async def keqing_build(ctx):
    embed = discord.Embed(title='Build(s) for Keqing')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Yunlai Swordsmanship*\n' +
                    '2. Elemental Burst - *Starward Sword*\n' +
                    '3. Elemental Skill - *Stellar Restoration*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    '+18% ATK/+18% ATK\n' +
                    'Thundering Fury/+18% ATK', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%\n' +
                    '- For Goblet of Eonothem: Electro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% > Elemental Mastery', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Mistsplitter Reforged__\n' +
                    '__Primordial Jade Cutter__\n' +
                    '__Summit Shaper__\n' +
                    '__Aquila Favonia__\n' +
                    '__Lion\'s Roar__\n' +
                    '__The Black Sword__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def keqing_team(ctx):
    embed = discord.Embed(title='Team(s) for Keqing')
    embed.add_field(name='Electro-charged Team', value='Team composition:\n' +
                    '1. Keqing\n' +
                    '2. Hydro character\n' +
                    '3. Electro character character\n' +
                    '4. Pyro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Xingqiu__\n' +
                    '__Sangonomiya Kokomi__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Jean__\n' +
                    '__Bennett__\n' +
                    '__Fischl__\n' +
                    '__Beidou__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Mono Electro Team', value='Team composition:\n' +
                    '1. Keqing\n' +
                    '2. Beidou\n' +
                    '3. Electro character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Fischl__\n' +
                    '__Kujou Sara__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Jean__\n' +
                    '__Sucrose__\n' +
                    '__Bennett__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)