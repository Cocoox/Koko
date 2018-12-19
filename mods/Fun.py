# "Fun" commands of Koko.

import discord, asyncio
from discord.ext import commands

import random
import re
import urllib.parse, urllib.request

class Fun:
    def __init__(self, bot):
        self.bot = bot
        self.send_message = bot.send_message0

    @commands.command(pass_context=True, aliases=['flipacoin','coinflip'])
    async def coin(self, ctx):
        ans = ['Heads!','Tails!']
        ans = random.choice(ans)
        await self.send_message(ctx.message.channel, ans)

    # test command, delete later
    @commands.command(pass_context=True)
    async def say(self, ctx, words:str):
        """Bot says what you say."""
        await self.send_message(ctx.message.channel, words)

def setup(bot):
    bot.add_cog(Fun(bot))