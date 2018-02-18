import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = ".")
description = 'RBMK Test Bot'

@bot.command()
async def beep(ctx):
    await ctx.send("boop")

## Initialize Bot
bot.run('NDE0NTI3OTY3MjAxMzI5MTYy.DWoq1Q.1aW-qKYa1TJFM776ECtlmQ9f9e0')
