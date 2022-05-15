import discord

async def hutao_build(ctx):
    embed = discord.Embed(title='Build(s) for Hu Tao')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Secret Spear of Wangsheng*\n' +
                    '2. Elemental Skill - *Guide to Afterlife*\n' +
                    '3. Elemental Burst - *Spirit Soother*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Crimson Witch of Flames\n' +
                    'Shimenawa\'s Reminiscence', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: HP%/Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Pyro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > Elemental Mastery > HP% > ATK%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Staff of Homa__\n' +
                    '__Dragon\'s Bane__\n' +
                    '__Deathmatch__\n' +
                    '__Primordial Jade Winged-Spear__\n' +
                    '__Lithic Spear__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def hutao_team(ctx):
    embed = discord.Embed(title='Team(s) for Hu Tao')
    embed.add_field(name='Resistance Shred Vaporized Team', value='Team composition:\n' +
                    '1. Hu Tao\n' +
                    '2. Xingqiu\n' +
                    '3. Anemo character\n' +
                    '4. Pyro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Thoma__\n' +
                    '__Amber__\n' +
                    '__Xinyan__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Flexible Vaporized Team', value='Team composition:\n' +
                    '1. Hu Tao\n' +
                    '2. Xingqiu\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Fischl__\n' +
                    '__Kaeya__\n' +
                    '__Albedo__\n' +
                    '__Yun Jin__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Double Geo Team', value='Team composition:\n' +
                    '1. Hu Tao\n' +
                    '2. Xingqiu\n' +
                    '3. Geo character\n' +
                    '4. Geo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhongli__\n' +
                    '__Albedo__\n' +
                    '__Yun Jin__\n' +
                    '__Noelle__\n' +
                    '__Traveler__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)