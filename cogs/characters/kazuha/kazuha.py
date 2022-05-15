import discord

async def kazuha_build(ctx):
    embed = discord.Embed(title='Build(s) for Kaedehara')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Kazuha Slash*\n' +
                    '2. Normal Attack - *Garyuu Bladework*\n' +
                    '3. Elemental Skill - *Chihayaburu*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Viridescent Venerer', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Elemental Mastery\n' +
                    '- For Circlet of Logos: Elemental Mastery', inline=True)
    embed.add_field(name='Substats Priority', value='Elemental Mastery > Energy Recharge% >= Crit Rate%/Crit DMG% > ATK%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Freedom-Sworn__\n' +
                    '__Jade Cutter__\n' +
                    '__Mistsplitter Reforged__\n' +
                    '__Skyward Blade__\n' +
                    '__Summit Shaper__\n' +
                    '__Iron Sting__\n' +
                    '__Favonius Sword__\n' +
                    '__Sacrificial Sword__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def kazuha_team(ctx):
    embed = discord.Embed(title='Team(s) for Kaedehara Kazuha')
    embed.add_field(name='Ganyu Melt Team', value='Team composition:\n' +
                    '1. Ganyu\n' +
                    '2. Pyro character\n' +
                    '3. Flexible\n' +
                    '4. Kaedehara Kazuha', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Bennett__\n' +
                    '__Xiangling__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Childe Vaporized Team', value='Team composition:\n' +
                    '1. Childe\n' +
                    '2. Xiangling\n' +
                    '3. Bennett\n' +
                    '4. Kaedehara Kazuha', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Freeze Team', value='Team composition:\n' +
                    '1. Kamisato Ayaka\n' +
                    '2. Cryo character\n' +
                    '3. Hydro character\n' +
                    '4. Kaedehara Kazuha', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Ganyu__\n' +
                    '__Mona__\n' +
                    '__Sangonomiya Kokomi__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Raiden "National" Team', value='Team composition:\n' +
                    '1. Raiden Shogun\n' +
                    '2. Xingqiu\n' +
                    '3. Kaedehara Kazuha\n' +
                    '4. Bennett', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)