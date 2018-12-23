# "Fun" commands of Koko.

import discord, asyncio
from discord.ext import commands

import random
import logging
import re
import urbandict
import brainyquote

log = logging.getLogger('koko')

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['coinflip'])
    async def coin(self, ctx):
        answer = ['Heads!','Tails!']
        answer = random.choice(answer)
        await self.bot.send_message(ctx.message.channel, answer)

    @commands.command(pass_context=True, aliases=['urb'])
    async def urban(self, ctx, *, word:str):
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
    
    @commands.command(pass_context=True)
    async def quote(self, ctx, topic:str=None):
        if topic is None:
            quote = brainyquote.pybrainyquote.get_random_quote()
        else:
            quote = brainyquote.pybrainyquote.get_quotes(topic.lower())
        try:
            quote = str(quote[0])
        except IndexError:
            log.error('InvalidTopic, user informed')
            await self.bot.send_message(ctx.message.channel, 'Topic not found.')
            return
        if quote.startswith('<img'):
            regex = re.compile(r'(url=")(.+)("\sid=)')
            match = regex.findall(quote)
            url = match[0][1]
            link = 'https://www.brainyquote.com/' + url
            await self.bot.send_message(ctx.message.channel, link)
            return
        await self.bot.send_message(ctx.message.channel, '*"{}"*'.format(quote))

def setup(bot):
    bot.add_cog(Fun(bot))