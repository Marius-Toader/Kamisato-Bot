import discord

async def ganyu_build(ctx):
    embed = discord.Embed(title='Build(s) for Ganyu')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Liutian Archery*\n' +
                    '2. Elemental Burst - *Celestial Shower*\n' +
                    '3. Elemental Skill - *Trail of the Qilin*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Wanderer\'s Troupe\n' +
                    'Shimenawa\'s Reminiscence\n' +
                    'Blizzard Strayer', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%\n' +
                    '- For Goblet of Eonothem: Cryo DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% > Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Amos\' Bow__\n' +
                    '__Thundering Pulse__\n' +
                    '__Polar Star__\n' +
                    '__Skyward Harp__\n' +
                    '__Hamayumi__\n' +
                    '__Blackcliff Warbow__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def ganyu_team(ctx):
    embed = discord.Embed(title='Team(s) for Ganyu')
    embed.add_field(name='Melt Team', value='Team composition:\n' +
                    '1. Ganyu\n' +
                    '2. Pyro character\n' +
                    '3. Anemo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Thoma__\n' +
                    '__Zhongli__\n' +
                    '__Xiangling__\n' +
                    '__Bennett__\n' +
                    '__Jean__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Freeze Team', value='Team composition:\n' +
                    '1. Ganyu\n' +
                    '2. Hydro character\n' +
                    '3. Cryo character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Mona__\n' +
                    '__Sangonomiya Kokomi__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Jean__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)