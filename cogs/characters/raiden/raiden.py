import discord

async def raiden_build(ctx):
    embed = discord.Embed(title='Build(s) for Raiden Shogun')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Secret Art: Musou Shinsetsu*\n' +
                    '2. Elemental Skill - *Transcendence: Baleful Omen*\n' +
                    '3. Normal Attack - *Origin*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Embelm of Severed Fate', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: Energy Recharge%/ATK%\n' +
                    '- For Goblet of Eonothem: Electro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% >= Energy Recharge%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Engulfing Lightning__\n' +
                    '__Staff of Homa__\n' +
                    '__Primordial Jade Winged-Spear__\n' +
                    '__Calamity Queller__\n' +
                    '__Skyward Spine__\n' +
                    '__“The Catch”__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)
    
async def raiden_team(ctx):
    embed = discord.Embed(title='Team(s) for Raiden Shogun')
    embed.add_field(name='Double Electro Team', value='Team composition:\n' +
                    '1. Raiden Shogun\n' +
                    '2. Electro character\n' +
                    '3. Anemo character\n' +
                    '4. Pyro/Hydro character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Jean__\n' +
                    '__Bennett__\n' +
                    '__Xiangling__\n' +
                    '__Kujou Sara__\n' +
                    '__Fischl__\n' +
                    'Yae Miko\n' +
                    '__Kokomi__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Triple Electro Team', value='Team composition:\n' +
                    '1. Raiden Shogun\n' +
                    '2. Electro character\n' +
                    '3. Electro character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    'Yae Miko\n' +
                    '__Kujou Sara__\n' +
                    '__Fischl__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Jean__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Raiden National Team', value='Team composition:\n' +
                    '1. Raiden Shogun\n' +
                    '2. Xingqiu\n' +
                    '3. Xiangling\n' +
                    '4. Bennett', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)