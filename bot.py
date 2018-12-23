# Runs the bot.

from koko import Koko
import logging

logging.basicConfig(format='[%(asctime)s][%(levelname)s] : %(message)s', level=logging.INFO)
log = logging.getLogger('koko')

token = 'NTE4NzQ3NzY4MzQ5NjU1MDUw.DvwKKA.s-NqXlKNT5Q-RtPC-Ei1O5CSN_M'

# with open("token.txt", "r") as tokenfile:
#     token = tokenfile.read()

bot = Koko(token=token)
log.info('starting bot')
bot.run()