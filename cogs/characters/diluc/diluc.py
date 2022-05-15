import discord

async def diluc_build(ctx):
    embed = discord.Embed(title='Build(s) for Diluc')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Skill - *Searing Onslaught*\n' +
                    '2. Normal Attack - *Tempered Sword*\n' +
                    '3. Elemental Burst - *Dawn*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Crimson Witch of Flames', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%/Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Pyro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > Elemental Mastery >= ATK%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Serpent Spine__\n' +
                    '__Redhorn Stonethresher__\n' +
                    '__Wolf\'s Gravestone__\n' +
                    '__The Unforged__\n' +
                    '__Rainslasher__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def diluc_team(ctx):
    embed = discord.Embed(title='Team(s) for Diluc')
    embed.add_field(name='Vaporized Team', value='Team composition:\n' +
                    '1. Diluc\n' +
                    '2. Xingqiu\n' +
                    '3. Bennett\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Sucrose__\n' +
                    '__Zhongli__\n' +
                    '__Jean__\n' +
                    '__Diona__\n' +
                    '__Kaedehara Kazuha__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Melt Team', value='Team composition:\n' +
                    '1. Diluc\n' +
                    '2. Bennett\n' +
                    '3. Cryo character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Rosaria__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Mono Pyro Team', value='Team composition:\n' +
                    '1. Diluc\n' +
                    '2. Pyro character\n' +
                    '3. Anemo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Albedo__\n' +
                    '__Xiangling__\n' +
                    '__Bennett__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)