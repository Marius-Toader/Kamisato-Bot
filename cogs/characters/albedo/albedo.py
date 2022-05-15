import discord

async def albedo_build(ctx):
    embed = discord.Embed(title='Build(s) for Albedo')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Skill - *Abiogenesis: Solar Isotoma*\n' +
                    '2. Elemental Burst - *Rite of Progeniture: Tectonic Tide*\n' +
                    '3. Normal Attack - *Favonius Bladework - Weiss*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Husk of Opulent Dreams', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: DEF%\n' +
                    '- For Goblet of Eonothem: Geo DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > DEF% > ATK% > Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Cinnabar Spindle__\n' +
                    '__Primordial Jade Cutter__\n' +
                    '__Harbinger of Dawn__\n' +
                    '__Festering Desire__\n' +
                    '__Mistsplitter Reforged__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def albedo_team(ctx):
    embed = discord.Embed(title='Team(s) for Albedo')
    embed.add_field(name='Double Geo Team', value='Team composition:\n' +
                    '1. Albedo\n' +
                    '2. Geo character\n' +
                    '3. Flexible\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Zhognli__\n' +
                    '__Ningguang__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)