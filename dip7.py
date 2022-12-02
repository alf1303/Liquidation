from utils import get_contract_data, get_duration_from_blocks, get_height

farmss = [
"3PKbd7pfmyaKWt6msaNAXyYUkuaumpea3bb",
"3P3y8NLGLYDx9obVaBF8je9uPTy2BDaK5n4",
"3PEVpbeDDkjmKqiMm25MgMZfazR7U1Eivzi",
"3PDs3ewniAQCp4LfXPMEqb2xRECgtZu2AR5",
"3PB8FTBTa1JspbXf8GiZTCdhYoq86QC6zxN",
"3P6gnGQpT9iEABEy5AxMzMbm6ijGHSvXyeb",
"3PJc5HTXgVWL7CYCec3huKJUtTPwJCNmMDF",
"3PEv4CE8moSLoAJw5y1bkiRMhtUF1nPRTfx",
"3P3ohGCRmJzjTsP7RQ7jZV7QNw76wB1Nsnn",
"3P5me5qyR7z28WDkCiW172coLxpRZvqzeNv",
"3PJroXdKXF21FmcRjY6z7osZPP8VUY5R5Go",
"3P6SQ4yDPRSzwk2nQD7ipK3HtxaEBX3M7Jk",
"3P7iSFkjVr74EQqwExsg7DWRXX2SMn3BA3n",
"3P3UMGin66fAe39AhJf5whS2Yabu6dZAmCF",
"3PCMKXu9r2ZNSxuLgnwoPXsWYhq6nMDADNo",
"3PEaA3SJb6wrfc2D4TPYTZ2xmMsufd7rCFJ"
]

class Voter():
    def __init__(self, address):
        self.address = address
        self.voted = False
        self.vote = None
        self.my_votes = {}


    def set_power(self, vote_power):
        self.vote_power = vote_power

    def set_vote(self, vote):
        self.vote = vote
        self.voted = True
    
    def __str__(self):
        sign = "" if not self.voted else "+" if self.vote else "-"
        return f"{self.address}: {round(self.vote_power/10**8, 3)} *{sign}*"

class Dip7_Voter():
    def __init__(self):
        self.top_count = 8
        self.curr_height = 0
        self.vote_height_start = 0
        self.vote_duration = 10000
        self.vote_contract = "3P38c43ME7gAtDWoM9NqA6juRMzjF2Uxz3b"
        self.vote_id = "Unknown"
        self.data = {}
        self.power_tops = []
        self.for_tops = []
        self.against_tops = []

        # self.info = "Collective Farms removed from calculations"
        self.time_left = "........"
        self.stats_str = "updating..."
        self.power_tops_str = "updating..."
        self.for_tops_str = "updating..."
        self.against_tops_str = "updating..."

    def set_time_left(self):
        try:
            self.curr_height = get_height()
            self.time_left = get_duration_from_blocks((self.vote_height_start + self.vote_duration) - self.curr_height)
        except Exception as e:
            print(f"Error while setting time left: {repr(e)}")

    def get_str_info(self):
        voted = 0
        voted_for = 0
        voted_against = 0
        total_vote_power = 0
        voted_power = 0
        voted_for_power = 0
        voted_against_power = 0
        voted_ratio = 0
        voted_for_percent = 0 # from voted
        voted_against_percent = 0 # from voted
        for el in self.data:
            voter: Voter
            voter = self.data[el]
            total_vote_power += voter.vote_power
            if voter.voted:
                voted += 1
                voted_power += voter.vote_power
                if voter.vote:
                    voted_for += 1
                    voted_for_power += voter.vote_power
                else:
                    voted_against += 1
                    voted_against_power += voter.vote_power
        voted_ratio = self.get_perc(voted_power, total_vote_power)
        voted_for_percent = self.get_perc(voted_for_power, voted_power)
        voted_against_percent = self.get_perc(voted_against_power, voted_power)
        resstr = ""
        resstr += f"*Vote ID: {self.vote_id}*\n"
        resstr += f"Total vote power: {round(total_vote_power/10**8, 3)}\n"
        resstr += f"Voted: *{voted} players, {voted_ratio}%* of total power\n"
        resstr += f"TRUE: *{voted_for} players, {voted_for_percent}%* of voted power\n"
        resstr += f"FALSE: *{voted_against} players, {voted_against_percent}%* of voted power\n"
        self.stats_str = resstr

        
    def get_perc(self, value, main_val):
        try:
            perc = (value/main_val)*100
            return round(perc, 3)
        except:
            return 0

    def get_voter(self, address):
        return self.data.get(address, Voter(address)) 

    def get_tops(self):
        self.power_tops = sorted(self.data.values(), key=lambda x: x.vote_power, reverse=True)
        voted_true = [self.data[el] for el in self.data if self.data[el].vote == True]
        self.for_tops = sorted(voted_true, key=lambda x: x.vote_power, reverse=True)
        voted_false = [self.data[el] for el in self.data if self.data[el].vote == False]
        self.against_tops = sorted(voted_false, key=lambda x: x.vote_power, reverse=True)

    def make_tops_str(self):
        self.power_tops_str = self.arr_to_str(self.power_tops)
        self.for_tops_str = self.arr_to_str(self.for_tops)
        self.against_tops_str = self.arr_to_str(self.against_tops)
        
    def arr_to_str(self, arr_in):
        res = ""
        arr = arr_in[:self.top_count]
        for el in arr:
            res += str(el) + "\n"
        return res

    def map_to_str(self, map):
        res = ""
        for idx,el in enumerate(map):
            res += f"   {idx}) {el}: {str(map[el])}\n"
        return res

    def get_my_info(self, address):
        res = f"Current: {self.vote_id}"
        if address in self.data:
            voter = self.data[address]
            res += f"*{address}:*\n"
            res += f"Vote power: {round(voter.vote_power/10**8, 3)}\n"
            res += "Votes:\n"
            res += self.map_to_str(voter.my_votes)
            return res
        else:
            return "No entries found"

    def fetch_fill_data(self):
        data = get_contract_data(address=self.vote_contract)
        for el in data:
            if el["key"] == "CURRENT_VOTE_IDENTIFIER":
                self.vote_id = el["value"]
            if el["key"] == f"VOTE_HEIGHT_START_{self.vote_id}":
                self.vote_height_start = int(el["value"])
            if "user_"  in el["key"] and "_vote-power" in el["key"]:
                arr = el["key"].split("_")
                address = arr[1]
                if address not in farmss:
                    power = int(el["value"])
                    voter = self.get_voter(address)
                    voter.set_power(power)
                    self.data[address] = voter
            key = f"_identifier_{self.vote_id}_vote"
            if "user_"  in el["key"] and "_identifier_" in el["key"] and "_vote" in el["key"]:
                arr = el["key"].split("_")
                address = arr[1]
                vote_id = arr[3]
                vote = True if el["value"] == "true" else False
                voter = self.get_voter(address)
                if self.vote_id == vote_id:
                    voter.set_vote(vote)
                voter.my_votes[vote_id] = vote
                self.data[address] = voter
        self.get_str_info()
        self.get_tops()
        self.make_tops_str()
        self.set_time_left()
        # print("data filled")


