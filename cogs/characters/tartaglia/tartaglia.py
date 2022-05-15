import discord

async def tartaglia_build(ctx):
    embed = discord.Embed(title='Build(s) for Tartaglia')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Skill - *Foul Legacy: Raging Tide*\n' +
                    '2. Elemental Burst - *Havoc: Obliteration*\n' +
                    '3. Normal Attack - *Cutting Torrent*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Heart of Depth\n' +
                    'Shimenawa\'s Reminiscence', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%\n' +
                    '- For Goblet of Eonothem: Hydro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% > Elemental Mastery% > Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Polar Star__\n' +
                    '__Thundering Pulse__\n' +
                    '__Skyward Harp__\n' +
                    '__Viridescent Hunt__\n' +
                    '__Amos\' Bow__\n' +
                    '__Rust__\n' +
                    '__Mouun\'s Moon__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def tartaglia_team(ctx):
    embed = discord.Embed(title='Team(s) for Hu Tao')
    embed.add_field(name='Vaporized Team', value='Team composition:\n' +
                    '1. Tartaglia\n' +
                    '2. Xiangling\n' +
                    '3. Bennett\n' +
                    '4. Anemo characer', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Jean__\n' +
                    '__Traveler__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Electro-charged Team', value='Team composition:\n' +
                    '1. Tartaglia\n' +
                    '2. Beidou\n' +
                    '3. Bennett\n' +
                    '4. Electro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Fischl__\n' +
                    '__Kujou Sara__\n' +
                    '__Traveler__\n' +
                    '__Albedo__\n' +
                    '__Yun Jin__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Single-target Electro-charged Team', value='Team composition:\n' +
                    '1. Tartaglia\n' +
                    '2. Fischl\n' +
                    '3. Bennett\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Albedo__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Jean__\n' +
                    '__Venti__\n' +
                    '__Kujou Sara__\n' +
                    '__Xingqiu__\n' +
                    '__Traveler__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)