# Runs the bot.

from koko import Koko
import logging

logging.basicConfig(format='[%(asctime)s][%(levelname)s] : %(message)s', level=logging.INFO)
log = logging.getLogger('koko')

with open("token.txt", "r") as tokenfile:
    token = tokenfile.read()

bot = Koko(token=token)
log.info('starting bot')
bot.run()