import discord

async def arataki_itto_build(ctx):
    embed = discord.Embed(title='Build(s) for Arataki Itto')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Normal Attack - *Fight Club Legends*\n' +
                    '2. Elemental Burst - *Royal Descent: Behold Itto the Evil!*\n' +
                    '3. Elemental Skill - *Masatsu Zetsugi: Akaushi Burst!*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Husk of Opulent Dreams\n' +
                    'Retracing Bolide', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: DEF%\n' +
                    '- For Goblet of Eonothem: Geo DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > Energy Recharge > DEF%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Redhorn Stonethresher__\n' +
                    '__Serpent Spine__\n' +
                    '__Skyward Pride__\n' +
                    '__Whiteblind__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def arataki_itto_team(ctx):
    embed = discord.Embed(title='Team(s) for Arataki Itto')
    embed.add_field(name='Triple Geo Team', value='Team composition:\n' +
                    '1. Arataki Itto\n' +
                    '2. Gorou\n' +
                    '3. Geo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Albedo__\n' +
                    '__Zhongli__\n' +
                    '__Traveler__\n' +
                    '__Ningguang__\n' +
                    '__Bennett__\n' +
                    '__Diona__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Mono Geo Team', value='Team composition:\n' +
                    '1. Arataki Itto\n' +
                    '2. Gorou\n' +
                    '3. Albedo\n' +
                    '4. Zhongli', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)