
class Transaction():
    anotherAddr = ""
    dApp = ""
    function = ""
    direction = ""
    def __init__(self, addr, id, type, timestamp, height, tr):
        self.address = addr
        self.id = id
        self.type = type
        self.timestamp = timestamp
        self.height = height
        self.outcome = {}
        self.income = {}
        self.tr = tr

class Asset():
    id = ""
    name = ""
    decimals = 0
    scale = 0
    amount = 0

    def __init__(self, id, name, decimals):
        self.id = id
        self.name = name
        self.decimals = decimals
        self.scale = int(10 ** decimals)

    def __str__(self):
        res = self.name + ": " + self.id + ", decimals: " + str(self.decimals)
        return res
    
    def prnt(self):
        val = self.amount/10 ** self.decimals
        res = "    " + str(round(val, 8)) + " " + self.name
        return res

class DaylyEarning():
    date = None
    amount = 0
    stakedEagles = 77
    stakedAnias = 150

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def __str__(self): 
        return f'{self.date} {self.amount/10**6}'
    