
from utils import get_contract_data

class Address():
    def __init__(self, address: str, vote: str, status: str, staked):
        self.address = address
        self.staked = 0
        self.vote = ""
        self.status = status

class Results():
    def __init__(self):
        self.voted_for = 0
        self.voted_against = 0
        self.votes_for = 0
        self.votes_against = 0
        self.votes = 0
        self.voted = 0
        self.voted_staked = 0
        self.global_staked = 0

    def clear(self):
        self.voted_for = 0
        self.voted_against = 0
        self.votes_for = 0
        self.votes_against = 0
        self.votes = 0
        self.voted = 0
        self.voted_staked = 0
        self.global_staked = 0

    def __str__(self):
        res = ""
        perc = round((self.voted_staked/self.global_staked)*100, 2)
        diff = self.voted_for - self.voted_against
        sign = "+++" if diff >= 0 else "---"
        res += f"*Voting for changing Buyback Ratio for PLUTO Protocol*\n"
        res += f"Status: *{sign} {round(diff/10**8, 4)} sPLUTO*\n"
        res += f"YES votes: *{self.votes_for} ({round(self.voted_for/10**8, 2)} sPLUTO, {round(self.voted_for*100/(self.voted_for + self.voted_against), 3)}% of voted)*\n"
        res += f"NO votes: *{self.votes_against} ({round(self.voted_against/10**8, 2)} sPLUTO, {round(self.voted_against*100/(self.voted_for + self.voted_against), 3)}% of voted)*\n"
        res += f"TOTAL votes: *{self.votes_for + self.votes_against} ({round(self.voted_staked/10**8, 3)} sPLUTO, {perc}% of staked)*"
        return res

def upd_results(results):
    pluto_vote1_contract = "3P3urybcgohip3uYE1hWF89gBPDKM3zLoMB"
    pluto_staking = "3P7dGTVZp8VLDYy3XEaUQbiqfi9cMK1Ly5q"
    data = get_contract_data(address=pluto_vote1_contract, regex="vote1.*")
    data_stake = get_contract_data(address=pluto_staking, regex="3P.*_sPluto||global_sPluto")
    stakers = {}
    results.clear()
    for el in data_stake:
        if el["key"] == "global_sPluto":
            results.global_staked = int(el["value"])
        adr = el["key"].split("_")[0]
        val = int(el["value"])
        stakers[adr] = val
    voters = {}
    for el in data:
        if len(el['key']) == 41:
            addr = el["key"].split("_")[1]
            vote = el["value"]
            staked = stakers.get(addr, 0)
            if vote == "yes":
                status = True
                results.votes_for += 1
                results.voted_for += staked
            if vote == "no":
                status = False
                results.votes_against += 1
                results.voted_against += staked
            results.voted += 1
            results.voted_staked += staked
            adr = Address(address=addr, vote=vote, status=status, staked=staked)
            voters[addr] = adr

