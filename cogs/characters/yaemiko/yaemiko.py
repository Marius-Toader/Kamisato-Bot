import discord

async def yae_miko_build(ctx):
    embed = discord.Embed(title='Build(s) for Yae Miko')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Skill - *Yakan Evocation: Sesshou Sakura*\n' +
                    '2. Elemental Burst - *Great Secret Art: Tenko Kenshin*\n' +
                    '3. Normal Attack - *Spiritfox Sin-Eater*', inline=False)
    embed.add_field(name='Artifact Set', value=
                    'Thundering Fury/+18% ATK\n' +
                    'Emblem of Severed Fate', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%/Energy Recharge%\n' +
                    '- For Goblet of Eonothem: Electro DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit Rate Bonus%/Crit DMG Bonus%', inline=True)
    embed.add_field(name='Substats Priority', value='Crit Rate%/Crit DMG% > Energy Recharge% > ATK% > Elemental Mastery%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Kagura\'s Verity__\n' +
                    '__Skyward Atlas__\n' +
                    '__Memory of Dust__\n' +
                    '__Lost Prayer to the Sacred Winds__\n' +
                    '__The Widsith__\n' +
                    '__Oathsworn\'s Eye__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def yae_miko_team(ctx):
    embed = discord.Embed(title='Team(s) for Yae Miko')
    embed.add_field(name='Double Electro Vaporized Team', value='Team composition:\n' +
                    '1. Yae Miko\n' +
                    '2. Raiden Shogun\n' +
                    '3. Anemo character\n' +
                    '4. Flexible', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Kaedehara Kazuha__\n' +
                    '__Jean__\n' +
                    '__Sayu__\n' +
                    '__Bennett__\n' +
                    '__Zhongli__\n' +
                    '__Venti__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Overload Team', value='Team composition:\n' +
                    '1. Yae Miko\n' +
                    '2. Raiden Shogun\n' +
                    '3. Xiangling\n' +
                    '4. Bennett', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Electro-charged Team', value='Team composition:\n' +
                    '1. Yae Miko\n' +
                    '2. Electro character\n' +
                    '3. Hydro character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Fischl__\n' +
                    '__Raiden Shogun__\n' +
                    '__Beidou__\n' +
                    '__Sangonomiya Kokomi__\n' +
                    '__Tartaglia__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Jean__\n' +
                    '__Venti__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)