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
        self.top10 = []

    # def calc_top10(self):
    #     key = "_farm_staked"
    #     for el in self.data:
    #         if key in el[]

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

class Investor():
    def __init__(self, address, staked, share, vote):
        self.address = address
        self.staked = staked
        self.share = share
        self.vote = vote
