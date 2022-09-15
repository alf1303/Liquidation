from .user import User
from os.path import exists
from datetime import datetime

# Used for managing users entities
class UserManager():
    def __init__(self, default_deposit):
        self.users = {}
        self.default_deposit = default_deposit
        self.storage_file = "chat_ids.txt"
        self.deporequests_file = "deporequests.txt"
        if exists(self.storage_file):
            self.load_users() 

# create new user, add to internal dictionary and return its string representation
    def create_user(self, user_id, name):
        if not self.user_exists(user_id):
            user = User(id=user_id, name=name, deposit=self.default_deposit)
            self.users[str(user_id)] = user
            self.save_users()
            return user
        else:
            return self.get_user(user_id=user_id)

# add user to internal dictionary
    def add_user(self, user):
        self.users[user.id] = user

# remove user from internal dictionary
    def remove_user(self, user):
        self.users.pop(user.id)

# get user entity from internal dictionary
    def get_user(self, user_id):
        if self.user_exists(user_id):
            user_id = str(user_id)
            return self.users[user_id]

    def user_exists(self, user_id):
        user_id = str(user_id)
        return user_id in self.users

    def user_subscribed(self, user_id):
        user = self.get_user(user_id=user_id)
        if user != None:
            return user.is_subscribed()
        else:
            return False
    
    def get_subscribed_users_ids(self):
        subscr = [el for el in self.users if self.user_subscribed(el)]
        return subscr

    def user_have_depo(self, user_id):
        user = self.get_user(user_id=user_id)
        if user != None:
            return user.is_active()
        else:
            return False

    def get_user_deposit(self, user_id):
        user_id = str(user_id)
        if self.user_exists(user_id):
            user = self.get_user(user_id)
            return user.deposit

    def increment_deposit(self, user_id, amount=1):
        user_id = str(user_id)
        if self.user_exists(user_id):
            user: User = self.get_user(user_id)
            user.increment_depo(value=int(amount))
            self.save_users()
            return True

    def decrement_deposit(self, user_id, amount=1):
        user_id = str(user_id)
        if self.user_exists(user_id):
            user: User = self.get_user(user_id)
            user.decrement_depo(value=int(amount))
            self.save_users()

    def set_deposit(self, user_id):
        user_id = str(user_id)
        if self.user_exists(user_id):
            user: User = self.get_user(user_id)
            user.set_depo(value=int(self.default_deposit))
            self.save_users()

    def request_deposit(self, user_id, address):
        with open(self.deporequests_file, "a") as f:
            now = datetime.now()
            f.write(f"{now} {user_id} {address}")


    def save_users(self):
        with open(self.storage_file, "w") as f:
            f.write('\n'.join(f"{str(self.users[el])}" for el in self.users))

    def load_users(self):
        with open(self.storage_file, "r") as f:
            lines = f.readlines()
            for l in lines:
                arr = l.split(" ")
                id = arr[0].strip()
                name = arr[1].strip()
                subscribed = True if arr[2].strip() == "True" else False
                level = int(arr[3].strip())
                deposit = int(arr[4].strip())
                vip = int(arr[5].strip())
                user = User(id=id, name=name, subscribed=subscribed, level=level, deposit=deposit, vip=vip)
                self.add_user(user)