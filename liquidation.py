from datetime import datetime
from time import sleep
from classes import Farm
from constants import all_farms, all_farms_dict
from dip7 import Dip7_Voter
from global_utils import getContractData
import requests
import logging

from telegram_bot.telegram_bot import MyBot

logging.basicConfig(filename=f'liqui.log', encoding='utf-8', format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO, force=True)

voter = Dip7_Voter()

# # # t.me/WavesDucksVotingBot
telegram_bot_token = "5895360281:AAFBhA6GQbnzgqIVDsP66lkUJRdLxaEwvi0"
bot = MyBot(token=telegram_bot_token, default_deposit=15, voter=voter)
bot.send_to_me(msg="BOT STARTED!!!!")

PERIOD = 10 # seconds

last = datetime.now().timestamp()

def loglog(msg):
    logging.info(msg=msg)

def main():
    global last
    while True:
        # voter.fetch_fill_data()
        # sleep(5)
        try:
            now = datetime.now().timestamp()
            if now - last > PERIOD:
                last = now
                loglog("processing...")
                voter.fetch_fill_data()
        except Exception as e:
            exc = repr(e)
            print(exc)
            bot.send_to_me(exc)
            sleep(10)
    
if __name__ == "__main__":
    main()