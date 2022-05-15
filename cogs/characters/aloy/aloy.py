import discord

async def aloy_build(ctx):
    embed = discord.Embed(title='Build(s) for Aloy')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Prophecies Of Dawn*\n' +
                    '2. Elemental Skill - *Frozen Wilds*\n' +
                    '3. Normal Attack - *Rapid Fire*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Blizzard Strayer\n' +
                    'Emblem of Severed Fate', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%/Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Cryo DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% > Energy Recharge% > Elemental Mastery', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Polar Star__\n' +
                    '__Elegy for the End__\n' +
                    '__Skyward Harp__\n' +
                    '__Thundering Pulse__\n' +
                    '__The Stringless__\n' +
                    '__Viridescent Hunt__\n' +
                    '__Amos\' Bow__\n' +
                    '__Rust__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def aloy_team(ctx):
    embed = discord.Embed(title='Team(s) for Aloy')
    embed.add_field(name='Permafreeze Team', value='Team composition:\n' +
                    '1. Aloy\n' +
                    '2. Cryo character\n' +
                    '3. Hydro character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Jean__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Mona__\n' +
                    '__Sangonomiya Kokomi__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Quickswap Melt Team', value='Team composition:\n' +
                    '1. Aloy\n' +
                    '2. Bennett\n' +
                    '3. Xiangling\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Sucrose__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Jean__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Zhongli__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)