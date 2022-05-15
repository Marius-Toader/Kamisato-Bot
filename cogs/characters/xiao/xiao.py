import discord

async def xiao_build(ctx):
    embed = discord.Embed(title='Build(s) for Xiao')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Whirlwind Thrust*\n' +
                    '2. Elemental Burst - *Bane of All Evil*\n' +
                    '3. Elemental Skill - *Lemniscatic Wind Cycling*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Vermillion Hereafter\n' +
                    'Viridescent Venerer/+18% ATK', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%\n' +
                    '- For Goblet of Eonothem: Anemo DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% > Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Primordial Jade Winged-Spear__\n' +
                    '__Staff of Homa__\n' +
                    '__Vortex Vanquisher__\n' +
                    '__Calamity Queller__\n' +
                    '__Skyward Spine__\n' +
                    '__Deathmatch__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def xiao_team(ctx):
    embed = discord.Embed(title='Team(s) for Xiao')
    embed.add_field(name='Basic Xiao Team', value='Team composition:\n' +
                    '1. Xiao\n' +
                    '2. Anemo character\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Jean__\n' +
                    '__Sucrose__\n' +
                    '__Bennett__\n' +
                    '__Zhongli__\n' +
                    '__Fischl__\n' +
                    '__Diona__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Double Geo Team', value='Team composition:\n' +
                    '1. Xiao\n' +
                    '2. Anemo character\n' +
                    '3. Zhongli\n' +
                    '4. Geo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Albedo__\n' +
                    '__Traveler__\n' +
                    '__Ningguang__\n' +
                    '__Sucrose__\n' +
                    '__Jean__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Double Pyro Team', value='Team composition:\n' +
                    '1. Xiao\n' +
                    '2. Anemo character\n' +
                    '3. Bennett\n' +
                    '4. Pyro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Sucrose__\n' +
                    '__Jean__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Xiangling__\n' +
                    '__Thoma__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)