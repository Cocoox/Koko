# The core of Koko.

import discord
from discord.ext import commands

import logging
import asyncio
import re

log = logging.getLogger('koko')
logging.getLogger('discord').setLevel(logging.CRITICAL)

mods = ['mods.Fun']

class Koko(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', None)
        super().__init__(command_prefix=commands.when_mentioned_or('k.'), *args, **kwargs)
        self.remove_command('help')
        
    def run(self):
        super().run(self.token)
    
    async def on_ready(self):
        log.info('bot ready')
        for mod in mods:
            self.load_extension(mod)
        await self.change_presence(game=discord.Game(name='k.'))

    async def on_message(self, message):
        if message.content.lower().startswith('k.') and message.content.lower() != 'k.':
            regex = re.compile(r'(k\.)[\s]*(\w+)(.*)', re.I|re.X|re.S)
            match = regex.findall(message.content)
            if len(match) == 0:
                return
            match = match[0]
            command = match[1].lower()
            message.content = match[0].lower() + command + match[2]
            if command not in self.commands:
                return
            if message.author.id == self.user.id:
                return
            log.info('{0} - {1}'.format(command.lower(), message.author))
            await self.process_commands(message)

    async def help_command(self, ctx):
        if ctx.invoked_subcommand:
            cmd = ctx.invoked_subcommand
        else:
            cmd = ctx.command
        pages = self.formatter.format_help_for(ctx, cmd)
        for page in pages:
            page = page.strip('`')
            await self.send_message(ctx.message.channel, page)

    async def shorten(self, channel, message):
        if len(message) == 0:
            return
        split = [message[i:i + 1999] for i in range(0, len(message), 1999)]
        for s in split:
            await self.send_message(channel, s)
            await asyncio.sleep(0.21)

    async def on_command_error(self, e, ctx):
        if isinstance(e, commands.MissingRequiredArgument):
            log.error('{}, help sent'.format(type(e).__name__))
            await self.help_command(ctx)
        elif isinstance(e, commands.BadArgument):
            log.error('{}, help sent'.format(type(e).__name__))
            await self.help_command(ctx)
        else:
            log.critical('{0.__class__.__name__}: {0}'.format(e.original))