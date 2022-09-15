class User():
    def __init__(self, id, name="None", subscribed=False, level=2, deposit=10, vip=0):
        self.id = id
        self.name = name
        self.subscribed = subscribed
        self.level = level
        self.deposit = deposit
        self.vip = vip
    
    def __str__(self):
        res = f"{self.id} {self.name} {self.subscribed} {self.level} {self.deposit} {self.vip}"
        return res

    def decrement_depo(self, value):
        self.deposit -= value

    def increment_depo(self, value):
        self.deposit += value

    def set_depo(self, value):
        self.deposit = value

    def is_active(self):
        return True
        return self.deposit > 0

    def is_subscribed(self):
        return self.subscribed