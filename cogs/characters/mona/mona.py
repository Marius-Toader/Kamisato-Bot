import discord

async def mona_build(ctx):
    embed = discord.Embed(title='Build(s) for Mona')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Illusory Torrent*\n' +
                    '2. Elemental Skill - *Mirror Reflection of Doom*\n' +
                    '3. Normal Attack - *Ripple of Fate*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Heart of Depth\n' +
                    'Emblem of Severed Fate\n' +
                    'Wanderer\'s Troupe\n' +
                    'Noblesse Oblige', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%/Elemental Mastery\n' +
                    '- For Goblet of Eonothem: Pyro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > ATK% >= Energy Recharge% > Elemental Mastery', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Skyward Atlas__\n' +
                    '__The Widsith__\n' +
                    '__Mappa Mare__\n' +
                    '__Favonius Codex__\n' +
                    '__Prototype Amber__\n' +
                    'Thrilling Tales of Dragon Slayers', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def mona_team(ctx):
    embed = discord.Embed(title='Team(s) for Mona')
    embed.add_field(name='Sustained Vaporized Team', value='Team composition:\n' +
                    '1. Mona\n' +
                    '2. Bennett\n' +
                    '3. Xiangling\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Venti__\n' +
                    '__Zhongli__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Burst Vaporized Team', value='Team composition:\n' +
                    '1. Mona\n' +
                    '2. Bennett\n' +
                    '3. Anemo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Klee__\n' +
                    '__Yanfei__\n' +
                    '__Zhongli__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Electro-charged Team', value='Team composition:\n' +
                    '1. Mona\n' +
                    '2. Electro character\n' +
                    '3. Electro character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Fischl__\n' +
                    '__Baidou__\n' +
                    '__Kujou Sara__\n' +
                    '__Raiden Shogun__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Sucrose__\n' +
                    '__Traveler__\n' +
                    '__Zhongli__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)