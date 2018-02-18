import discord
import asyncio
import roads
import emoji
from random import getrandbits
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = ".")
description = 'RBMK Test Bot'


@bot.command()
async def status(ctx):
    roadReport = roads.road_condition()
    camSrc = "http://ns-webcams.its.sfu.ca/public/images/gaglardi-current.jpg?nocache=" + str(getrandbits(64)) + "&update=15000&timeout=1800000&offset=4"
    e = discord.Embed(title="Burnaby Mountain Status Update", color=0xffffff, description=roadReport)
    e.set_image(url=camSrc)
    msg = await ctx.send(embed=e)
    i = 0
    emojis = ['\U00000031\U000020e3', '\U00000032\U000020e3', '\U00000033\U000020e3', '\U00000034\U000020e3', '\U00000035\U000020e3', '\U00000036\U000020e3']
    for i in range(6):
        await msg.add_reaction(emojis[i])


## Initialize Bot
bot.run('NDE0NTI3OTY3MjAxMzI5MTYy.DWoq1Q.1aW-qKYa1TJFM776ECtlmQ9f9e0')
