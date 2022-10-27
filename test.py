
from utils import get_contract_data

class Address():
    def __init__(self, address: str, vote: str, status: str, staked):
        self.address = address
        self.staked = 0
        self.vote = ""
        self.status = status

class Results():
    def __init__(self):
        self.voted_1 = 0
        self.voted_2 = 0
        self.voted_3 = 0
        self.votes_1 = 0
        self.votes_2 = 0
        self.votes_3 = 0
        self.votes = 0
        self.voted = 0
        self.voted_staked = 0
        self.global_staked = 0

    def clear(self):
        self.voted_1 = 0
        self.voted_2 = 0
        self.voted_3 = 0
        self.votes_1 = 0
        self.votes_2 = 0
        self.votes_3 = 0
        self.votes = 0
        self.voted = 0
        self.voted_staked = 0
        self.global_staked = 0

    def __str__(self):
        res = ""
        perc = round((self.voted_staked/self.global_staked)*100, 2)
        res += f"*PLUTO voting step 2*\n"
        # res += f"Status: *{sign} {round(diff/10**8, 2)} sPLUTO*\n"
        res += f"*Option 1* votes: *{self.votes_1} ({round(self.voted_1/10**8, 2)} sPLUTO, {round(self.voted_1*100/(self.voted_1 + self.voted_2 + self.voted_3), 2)}% of voted)*\n"
        res += f"*Option 2* votes: *{self.votes_2} ({round(self.voted_2/10**8, 2)} sPLUTO, {round(self.voted_2*100/(self.voted_1 + self.voted_2 + self.voted_3), 2)}% of voted)*\n"
        res += f"*Option 3* votes: *{self.votes_3} ({round(self.voted_3/10**8, 2)} sPLUTO, {round(self.voted_3*100/(self.voted_1 + self.voted_2 + self.voted_3), 2)}% of voted)*\n"
        res += f"TOTAL votes: *{self.votes_1 + self.votes_2 + self.votes_3} ({round(self.voted_staked/10**8, 2)} sPLUTO, {perc}% of staked)*"
        return res

def upd_results(results):
    pluto_vote1_contract = "3P3urybcgohip3uYE1hWF89gBPDKM3zLoMB"
    pluto_staking = "3P7dGTVZp8VLDYy3XEaUQbiqfi9cMK1Ly5q"
    data = get_contract_data(address=pluto_vote1_contract, regex="vote2.*")
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
        # print(el)
        if len(el['key']) == 41:
            addr = el["key"].split("_")[1]
            vote = el["value"]
            staked = stakers.get(addr, 0)
            # print(vote)
            if vote == 1 or vote == "1":
                status = True
                results.votes_1 += 1
                results.voted_1 += staked
            if vote == 2 or vote == "2":
                status = False
                results.votes_2 += 1
                results.voted_2 += staked
            if vote == 3 or vote == "3":
                status = False
                results.votes_3 += 1
                results.voted_3 += staked
            if vote in ["1", "2", "3", 1, 2, 3]:
                results.votes += 1
                results.voted_staked += staked
                adr = Address(address=addr, vote=vote, status=status, staked=staked)
                voters[addr] = adr

