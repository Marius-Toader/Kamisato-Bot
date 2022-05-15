import discord

async def zhongli_build(ctx):
    embed = discord.Embed(title='Build(s) for Zhongli')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Skill - *Dominus Lapidis*\n' +
                    '2. Elemental Burst - *Planet Befall*\n' +
                    '3. Normal Attack - *Rain of Stone*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Tenacity of the Millelith\n' +
                    'Noblesse Oblige', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: HP%/ATK%\n' +
                    '- For Goblet of Eonothem: HP%/Geo DMG Bonus%\n' +
                    '- For Circlet of Logos: HP%/Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='HP% >= Crit Rate%/Crit DMG% > ATK%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Staff of Homa__\n' +
                    '__Primordial Jade Winged-Spear__\n' +
                    '__Vortex Vanquisher__\n' +
                    '__Deathmatch__\n' +
                    '__Skyward Spine__\n' +
                    '__Favonius Lance__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def zhongli_team(ctx):
    embed = discord.Embed(title='Team(s) for Zhongli')
    embed.add_field(name='Burst Support Team', value='Team composition:\n' +
                    '1. Zhongli\n' +
                    '2. Razon\n' +
                    '3. Rosaria\n' +
                    '4. Kaeya', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Double Geo Team', value='Team composition:\n' +
                    '1. Zhongli\n' +
                    '2. Geo character\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Albedo__\n' +
                    '__Traveler__\n' +
                    '__Ningguang__\n' +
                    '__Bennett__\n' +
                    '__Xingling__\n' +
                    '__Tartaglia__\n' +
                    '__Fischl__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Physical Carry Team', value='Team composition:\n' +
                    '1. Zhongli\n' +
                    '2. Geo character\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Albedo__\n' +
                    '__Ningguang__\n' +
                    '__Traveler__\n' +
                    '__Bennett__\n' +
                    '__Xiangling__\n' +
                    '__Xingqiu__\n' +
                    '__Rosaria__\n' +
                    '__Fischl__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)