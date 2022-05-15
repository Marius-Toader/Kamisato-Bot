import discord

async def yoimiya_build(ctx):
    embed = discord.Embed(title='Build(s) for Yoimiya')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Firework Flare-Up*\n' +
                    '2. Elemental Burst - *Ryuukin Saxifrage*\n' +
                    '3. Elemental Skill - *Niwabi Fire-Dance*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Crimson Witch of Flames\n' +
                    'Shimenawa\'s Reminiscence', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%/Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Pyro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% > Elemental Mastery > Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Thundering Pulse__\n' +
                    '__Polar Star__\n' +
                    '__Skyward Harp__\n' +
                    '__Amos\' Bow__\n' +
                    '__Rust__\n' +
                    '__Viridescent Hunt__\n' +
                    '__Hamayumi__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def yoimiya_team(ctx):
    embed = discord.Embed(title='Team(s) for Yoimiya')
    embed.add_field(name='Vaporized Team', value='Team composition:\n' +
                    '1. Yoimiya\n' +
                    '2. Xingqiu\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Jean__\n' +
                    '__Zhongli__\n' +
                    '__Yun Jin__\n' +
                    '__Bennett__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Overloaded Team', value='Team composition:\n' +
                    '1. Yoimiya\n' +
                    '2. Fischl\n' +
                    '3. Beidou\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Bennett__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Zhongli__\n' +
                    '__Yun Jin__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Double Pyro Team', value='Team composition:\n' +
                    '1. Yoimiya\n' +
                    '2. Bennett\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Albedo__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Xianglng__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)