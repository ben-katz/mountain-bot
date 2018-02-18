import discord
import asyncio
from discord.ext import commands
from discord.ext import commands
from discord.ext.commands import Bot

Client = discord.Client
client = commands.Bot(command_prefix = ".")
description = 'RBMK Test Bot'

@client.command()
async def beep(ctx):
    await ctx.send("boop")

## Initialize Bot
client.run('NDE0NTI3OTY3MjAxMzI5MTYy.DWoq1Q.1aW-qKYa1TJFM776ECtlmQ9f9e0')
