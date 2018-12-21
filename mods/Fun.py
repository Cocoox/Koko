# "Fun" commands of Koko.

import discord, asyncio
from discord.ext import commands

import random
import urbandict
import logging

log = logging.getLogger('koko')

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['coinflip'])
    async def coin(self, ctx):
        ans = ['Heads!','Tails!']
        ans = random.choice(ans)
        await self.bot.send_message(ctx.message.channel, ans)

    @commands.command(pass_context=True, aliases=['urb'])
    async def urban(self, ctx, word:str):
        """Get a definition from the urban dictionary."""
        try:
            urban = urbandict.define(word)
        except Exception as e:
            log.error('{}, user informed'.format(type(e).__name__))
            await self.bot.send_message(ctx.message.channel, 'No definition found.')
            return
        message = '`{0}`\n\n'.format(word.capitalize())
        message += '__Definition__ \n{0}\n\n'.format(urban[0]['def'])
        message += '__Example__ \n{0}'.format(urban[0]['example'])
        await self.bot.shorten(ctx.message.channel, message)

def setup(bot):
    bot.add_cog(Fun(bot))