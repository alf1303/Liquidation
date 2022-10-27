from utils import get_contract_data, get_contract_data_noreg

class Staker():
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount
        self.ratio = 1.19
    
    def __str__(self):
        return f"{self.address}: {round(self.amount/10**8, 2)}"

pluto_vote1_contract = "3P3urybcgohip3uYE1hWF89gBPDKM3zLoMB"
pluto_staking = "3P7dGTVZp8VLDYy3XEaUQbiqfi9cMK1Ly5q"
data = get_contract_data_noreg(address=pluto_vote1_contract)
data_stake = get_contract_data(address=pluto_staking, regex="3P.*_sPluto")

stakers = []
for el in data_stake:
    adr = el["key"].split("_")[0]
    amount = int(el["value"])
    staker = Staker(adr, amount)
    stakers.append(staker)

print(f"Stakers PLUTO: {len(data_stake)}")

voters_yes = []
voters_no = []

batch_yes = []
batch_no = []

for el in data:
    key = el["key"]
    if key.startswith("vote1_3P"):
        adr = key.split("_")[1]
        if el["value"] == "yes":
            voters_yes.append(adr)
        if el["value"] == "no":
            voters_no.append(adr)
    if "vote1_yes_batch" in key:
        adrs = el["value"].split(",")
        for a in adrs:
            if len(a) == 35 and a.startswith("3P"):
                batch_yes.append(a)
    if "vote1_no_batch" in key:
        adrs = el["value"].split(",")
        for a in adrs:
            if len(a) == 35 and a.startswith("3P"):
                batch_no.append(a)

stakers.sort(key=lambda x: x.amount, reverse=True)
for idx,s in enumerate(stakers):
    sign = ""
    if s.address in voters_yes:
        sign = "+"
    if s.address in voters_no:
        sign = "-"
    print(f"{idx}) {s} {sign}")

# voters_yes.sort()
# voters_no.sort()
# batch_yes.sort()
# batch_no.sort()

# print(len(voters_yes), len(batch_yes), len(voters_no), len(batch_no))

# for i in range(31):
#     a = "NONE" if i >= len(voters_yes) else voters_yes[i]
#     b = "NONE" if i >= len(batch_yes) else batch_yes[i]
#     print(a, b)

