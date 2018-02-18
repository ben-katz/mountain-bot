import discord
import asyncio
import roads
from random import getrandbits
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = ".")
description = 'RBMK Test Bot'

@bot.command()
async def status(ctx):
    j = 0
    camSrc = []
    roadReport = roads.road_condition()
    camSrc.append(str("http://ns-webcams.its.sfu.ca/public/images/aqn-current.jpg?nocache=" + str(getrandbits(64))) + "&update=15000&timeout=1800000&offset=4")
    camSrc.append("http://ns-webcams.its.sfu.ca/public/images/aqsw-current.jpg?nocache=" + str(getrandbits(64)) + "&update=15000&timeout=1800000&offset=4")
    camSrc.append("http://ns-webcams.its.sfu.ca/public/images/udn-current.jpg?nocache=" + str(getrandbits(64)) + "&update=15000&timeout=1800000&offset=4")
    camSrc.append("http://ns-webcams.its.sfu.ca/public/images/gaglardi-current.jpg?nocache=" + str(getrandbits(64)) + "&update=15000&timeout=1800000&offset=4")
    camSrc.append("http://ns-webcams.its.sfu.ca/public/images/towern-current.jpg?nocache=" + str(getrandbits(64)) + "&update=15000&timeout=1800000&offset=4")
    camSrc.append("http://ns-webcams.its.sfu.ca/public/images/towers-current.jpg?nocache=" + str(getrandbits(64)) + "&update=15000&timeout=1800000&offset=4")
    e = discord.Embed(title="Burnaby Mountain Status Update", color=0xffffff, description=roadReport)
    e.set_image(url=camSrc[j])
    msg = await ctx.send(embed=e)
    i = 0
    k = 0
    for i in range(6):
        e.set_image(url=camSrc[j])
        edit = await msg.edit(embed=e)
        j += 1
        await asyncio.sleep(2)


## Initialize Bot
bot.run('NDE0NTI3OTY3MjAxMzI5MTYy.DWoq1Q.1aW-qKYa1TJFM776ECtlmQ9f9e0')


#    for i in range(6):
#        await msg.add_reaction(emojis[i])
