class Farm():
    def __init__(self, dApp, asset_id, name):
        self.dApp = dApp
        self.asset_id = asset_id
        self.name = name

        self.decimals = 0
        self.asset_name = ""
        self.all_tokens = 0
        self.staked_amount = 0
        self.voted = 0
        self.voted_true = 0
        self.voted_false = 0
        self.quorum = 0

        self.data = []
        self.investors = []

    def calc_top10(self):
        self.investors.clear()
        key = "_farm_staked"
        for el in self.data:
            if key in el["key"]:
                addr = el["key"].split("_")[0]
                staked = el["value"]
                share = round(staked*100/self.staked_amount, 2)
                inv = Investor(address=addr, staked=staked, share=share, vote="")
                self.investors.append(inv)
        for inv in self.investors:
            vote_key = f"VOTE_{inv.address}"
            for el2 in self.data:
                if vote_key in el2["key"]:
                    if el2["value"] == "true":
                        inv.vote = "❌"
                    else:
                        inv.vote = "✔️"
                    break
                else:
                    inv.vote = ""
        self.investors.sort(key=lambda x: x.share, reverse=True)
        


    def calc_quorum(self):
        self.quorum = round(self.voted*100/self.all_tokens, 2)
    
    def get(self, value):
        v = value/10**self.decimals
        return round(v, 4)

    def __str__(self):
        quorum = round(self.voted*100/self.all_tokens, 2)
        if quorum > 35 and self.voted_false > self.voted_true:
            status = "😁"
        if quorum < 35 and quorum > 20:
            status = "😐"
        if quorum <= 20 or self.voted_false < self.voted_true:
            status = "🤢"
        res = f"*    {self.name:} Farm* {status}\n"
        res += f"Total tokens: {self.get(self.all_tokens)}\n"
        res += f"Staked tokens: {self.get(self.staked_amount)}\n"
        # try:
        #     res += f"Not Liquidate: {self.get(self.voted_false)}, {round(self.voted_false*100/self.voted, 2)}% of voted\n"
        #     res += f"Liquidate: {self.get(self.voted_true)}, {round(self.voted_true*100/self.voted, 2)}% of voted\n"
        # except ZeroDivisionError as e:
        #     res += "NO VOTES YET\n"
        # res += f"Voted: {self.get(self.voted)}, {round(self.voted*100/self.staked_amount, 2)}% of staked\n"

        try:
            res += f"Not Liquidate: {round(self.voted_false*100/self.voted, 2)}%\n"
            res += f"Liquidate: {round(self.voted_true*100/self.voted, 2)}%\n"
        except ZeroDivisionError as e:
            res += "NO VOTES YET\n"
        res += f"*Quorum: {quorum}%*, ({self.get(self.voted)})"
        return res

    def str_top10(self):
        res = ""
        for idx, el in enumerate(self.investors):
            if idx == 10:
                break
            res += f"{idx + 1}) {str(el)}\n"
        return res

class Investor():
    def __init__(self, address, staked, share, vote):
        self.address = address
        self.staked = staked
        self.share = share
        self.vote = vote

    def __str__(self):
        return f"{self.address} *{self.share}%* {self.vote}"
