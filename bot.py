import discord
import asyncio
import roads
from random import getrandbits
from discord.ext import commands
from discord.ext.commands import Bot

## Set Command Prefix & Description
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
    for i in range(6):
        e.set_image(url=camSrc[j])
        edit = await msg.edit(embed=e)
        j += 1
        await asyncio.sleep(2)


## Initialize Bot
bot.run('BOT_KEY_HERE')
