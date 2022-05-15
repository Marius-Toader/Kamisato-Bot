import discord
    
async def ayaka_build(ctx):
    embed = discord.Embed(title='Build(s) for Kamisato Ayaka')
    embed.add_field(name='Talent Upgrade Priority', value=
                    '1. Elemental Burst - *Kamisato Art: Soumetsu*\n' +
                    '2. Normal Attack - *Kamisato Art: Kabuki*\n' +
                    '3. Elemental Skill - *Kamisato Art: Hyouka*', inline=False)
    embed.add_field(name='Artifact Set', value='Blizzard Strayer', inline=False)
    embed.add_field(name='Main Stats', value=
                    '- For Sands of Eon: ATK%\n' +
                    '- For Goblet of Eonothem: Cryo DMG Bonus%\n' +
                    '- For Circlet of Logos: Crit DMG Bonus%/ATK%', inline=True)
    embed.add_field(name='Substats Priority', value='Energy Recharge% > Crit DMG% > ATK% >= Crit Rate%', inline=True)
    embed.add_field(name='Weapon Choices', value=
                    '__Mistsplitter Reforged__\n' +
                    '__Primordial Jade Cutter__\n' +
                    '__Summit Shaper__\n' +
                    '__Skyward Blade__\n' +
                    '__Aquila Favonia__\n' +
                    '__Amenoma Kageuchi__\n' +
                    '__The Black Sword__\n' +
                    '__Blackcliff Longsword__', inline=False)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)

async def ayaka_team(ctx):
    embed = discord.Embed(title='Team(s) for Kamisato Ayaka')
    embed.add_field(name='Freeze Team', value='Team composition:\n' +
                    '1. Kamisato Ayaka\n' +
                    '2. Cryo character\n' +
                    '3. Hydro character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Shenhe__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Ganyu__\n' +
                    '__Mona__\n' +
                    '__Sangonomiya Kokomi__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Venti__\n' +
                    '__Sucrose__', inline=True)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Mono Cryo Team', value='Team composition:\n' +
                    '1. Kamisato Ayaka\n' +
                    '2. Cryo character\n' +
                    '3. Cryo character\n' +
                    '4. Anemo character', inline=True)
    embed.add_field(name='Potential teammates', value=
                    '__Shenhe__\n' +
                    '__Diona__\n' +
                    '__Rosaria__\n' +
                    '__Kaedehara Kazuha__\n' +
                    '__Jean__', inline=True)
    embed.set_footer(text='Information courtesy of keqingmains.com')
    await ctx.send(embed=embed)