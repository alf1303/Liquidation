from datetime import datetime
from time import sleep
from classes import Farm
from constants import all_farms, all_farms_dict
from global_utils import getContractData
import requests

from telegram_bot.telegram_bot import MyBot
from test import Results, upd_results
from utils import get_contract_data, get_height, loglog

pluto_vote1_contract = "3P3urybcgohip3uYE1hWF89gBPDKM3zLoMB"

# # # https://t.me/TestDuckHuntAssistBot
# telegram_bot_token = "5636247410:AAFuQCje4a_LIzs4wocPVSegWlDXsFMQQYA"
results = Results()
telegram_bot_token = "5511483842:AAH1UxdJSoOxJqs_4WwffgKaSgb9ptgriRs" #- test
# telegram_bot_token = "5636247410:AAFuQCje4a_LIzs4wocPVSegWlDXsFMQQYA"
bot = MyBot(token=telegram_bot_token, default_deposit=15, results=results)
bot.send_to_me(msg="BOT STARTED!!!!")

PERIOD = 20 # seconds

last = datetime.now().timestamp()

# def main():
#     global last
#     while True:
#         now = datetime.now().timestamp()
#         if now - last > PERIOD:
#             last = now
#             loglog("processing...")
#             process_farms()

def main():
    global last
    while True:
        try:
            now = datetime.now().timestamp()
            if now - last > PERIOD:
                last = now
                loglog("processing...")
                process_pluto_vote()
        except Exception as e:
            exc = repr(e)
            print(exc)
            bot.send_to_me(exc)
            sleep(10)

def process_farms():
    tt = datetime.now()
    height = get_height()
    for f in all_farms:
        fill_global(f)
        fill_stake_vote(f)
        f.calc_quorum(height=height)
        f.calc_top10()
    loglog(f"time: {datetime.now() - tt} sec")
    bot.send_to_me("Parsing successful")

def process_pluto_vote():
    upd_results(results=results)


def fill_global(farm):
    asset_id = farm.asset_id
    req_str = f"https://nodes.wavesnodes.com/assets/details/{asset_id}"
    res = requests.get(req_str).json()
    if "error" not in res:
        farm.asset_name = res["name"]
        farm.decimals = res["decimals"]
        farm.all_tokens = res["quantity"]

def fill_stake_vote(farm: Farm):
    data = getContractData(farm.dApp)
    farm.data = data
    start_key = "VOTE_HEIGHT_START"
    staked_key = "global_staked"
    vote_false_key = "VOTE_TOTAL_false"
    vote_true_key = "VOTE_TOTAL_true"
    for el in data:
        if el["key"] == staked_key:
            farm.staked_amount = el["value"]
        if vote_false_key in el["key"]:
            farm.voted_false = el["value"] 
        if vote_true_key in el["key"]:
            farm.voted_true = el["value"]
        if start_key in el["key"]:
            farm.start = el["value"]
        farm.voted = farm.voted_false + farm.voted_true
    
if __name__ == "__main__":
    process_farms()
    main()