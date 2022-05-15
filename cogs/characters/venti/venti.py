import discord

async def venti_build(ctx):
    embed = discord.Embed(title='Build(s) for Venti')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Wind\'s Grand Ode*\n' +
                    '2. Elemental Skill - *Skyward Sonnet*\n' +
                    '3. Normal Attack - *Divine Marksmanship*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Viridescent Venerer', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Elemental Mastery\n' +
                    '- For Circlet of Logos: Elemental Mastery', inline=True)
    embed.add_field(name='Substats Priority', value='Elemental Mastery > Energy Recharge% > ATK% > Crit Rate%/Crit DMG%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Elegy for the End__\n' +
                    '__The Stringless__\n' +
                    '__Windblume Ode__\n' +
                    '__Favonius Warbow__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def venti_team(ctx):
    embed = discord.Embed(title='Team(s) for Venti')
    embed.add_field(name='Freeze Team', value='Team composition:\n' +
                    '1. Venti\n' +
                    '2. Ganyu\n' +
                    '3. Cryo character\n' +
                    '4. Hydro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Shenhe__\n' +
                    '__Mona__\n' +
                    '__Sangonomiya Kokomi__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Electro-charged Team', value='Team composition:\n' +
                    '1. Venti\n' +
                    '2. Hydro character\n' +
                    '3. Electro character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Mona__\n' +
                    '__Sangonomiya Kokomi__\n' +
                    '__Xingqiu__\n' +
                    '__Fischl__\n' +
                    '__Raiden Shogun__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Pyro Swirl Team', value='Team composition:\n' +
                    '1. Venti\n' +
                    '2. Kaedehara Kazuha\n' +
                    '3. Bennett\n' +
                    '4. Pyro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Klee__\n' +
                    '__Yoimiya__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)