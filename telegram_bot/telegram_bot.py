# USAGE:

# from telegram_bot.telegram_bot import MyBot
# # # https://t.me/TestDuckHuntAssistBot
# telegram_bot_token = "5511483842:AAH1UxdJSoOxJqs_4WwffgKaSgb9ptgriRs"
# bot = MyBot(token=telegram_bot_token, default_deposit=15)
# bot.send_to_me(msg="BOT STARTED!!!!")

from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler
import telegram
import re

from telegram_bot.user_manager import UserManager

class MyBot:
    """"""
    my_id = "681851428" # User ID of bot's Administrator Account

    def __init__(self, token, farms, default_deposit=15):
        self.bot = telegram.Bot(token=token)
        self.farms = farms
        self.calls = 0
        self.user_manager = UserManager(default_deposit=default_deposit)
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.initialize()
    
    def initialize(self):

        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

        # depo_handler = CommandHandler('depo', self.depo)
        # self.dispatcher.add_handler(depo_handler)

        help_handler = CommandHandler('help', self.help)
        self.dispatcher.add_handler(help_handler)

        # rset_handler = CommandHandler('rset', self.rset)
        # self.dispatcher.add_handler(rset_handler)

        # refill_handler = CommandHandler('refill', self.refill)
        # self.dispatcher.add_handler(refill_handler)

        # request_deposit_handler = CommandHandler('requestdepo', self.requestdepo)
        # self.dispatcher.add_handler(request_deposit_handler)

        allfarms_handler = CommandHandler('allfarms', self.allfarms)
        self.dispatcher.add_handler(allfarms_handler)

        turtle_handler = CommandHandler('turtle', self.turtle)
        self.dispatcher.add_handler(turtle_handler)

        duxplorer_handler = CommandHandler('duxplorer', self.duxplorer)
        self.dispatcher.add_handler(duxplorer_handler)

        math_handler = CommandHandler('mathematical', self.math)
        self.dispatcher.add_handler(math_handler)

        eggseggs_handler = CommandHandler('eggseggs', self.eggseggs)
        self.dispatcher.add_handler(eggseggs_handler)

        latam_handler = CommandHandler('latam', self.latam)
        self.dispatcher.add_handler(latam_handler)

        fomo_handler = CommandHandler('fomo', self.fomo)
        self.dispatcher.add_handler(fomo_handler)

        mundo_handler = CommandHandler('mundo', self.mundo)
        self.dispatcher.add_handler(mundo_handler)

        eggpoint_handler = CommandHandler('eggpoint', self.eggpoint)
        self.dispatcher.add_handler(eggpoint_handler)

        endoworld_handler = CommandHandler('endoworld', self.endoworld)
        self.dispatcher.add_handler(endoworld_handler)

        marvinfavis_handler = CommandHandler('marvinfavis', self.marvinfavis)
        self.dispatcher.add_handler(marvinfavis_handler)

        eggmoon_handler = CommandHandler('eggmoon', self.eggmoon)
        self.dispatcher.add_handler(eggmoon_handler)

        duckstreet_handler = CommandHandler('duckstreet', self.duckstreet)
        self.dispatcher.add_handler(duckstreet_handler)

        kolkhoz_handler = CommandHandler('kolkhoz', self.kolkhoz)
        self.dispatcher.add_handler(kolkhoz_handler)

        forklog_handler = CommandHandler('forklog', self.forklog)
        self.dispatcher.add_handler(forklog_handler)

        cgu_handler = CommandHandler('cgu', self.cgu)
        self.dispatcher.add_handler(cgu_handler)

        insiders_handler = CommandHandler('insiders', self.insiders)
        self.dispatcher.add_handler(insiders_handler)


        broadcast_handler = CommandHandler('broadcast', self.broadcast)
        self.dispatcher.add_handler(broadcast_handler)

        send_to_handler = CommandHandler('sendto', self.sendto)
        self.dispatcher.add_handler(send_to_handler)

        address_to_handler = CommandHandler('address', self.address)
        self.dispatcher.add_handler(address_to_handler)

        text_handler = MessageHandler(filters=Filters.text, callback=self.txt_handler)
        self.dispatcher.add_handler(text_handler)

        self.updater.start_polling()

# check if user id exists in storage
    def check_id(self, user_id):
        return True
        return self.user_manager.user_exists(user_id=user_id)

    def check_id_fake(self, user_id):
        return self.user_manager.user_exists(user_id=user_id)
    

    def send_to_all(self, msg):
        for el in self.user_manager.users:
            self.bot.send_message(chat_id=el, text=msg)

    def send_to_subscribed(self, msg):
        for el in self.user_manager.get_subscribed_users_ids:
            self.bot.send_message(chat_id=el, text=msg)

    def send_by_id(self, id, msg):
        allow = self.check_id(id)
        if allow:
            self.bot.send_message(chat_id=id, text=msg, parse_mode = "Markdown")
        else:
            self.bot.send_message(chat_id=id, text="Hello World")

    def send_to_me(self, msg):
        self.send_by_id(self.my_id, msg)

    ###########   SPECIAL METHODS   ###############

    def allfarms(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = ""
        for f in sorted(self.farms.values(), key= lambda x: x.quorum, reverse=True):
            msg += str(f) + "\n"
            msg += "-------------------------\n"
        self.send_by_id(id=user_id, msg=msg)

    def turtle(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["turtle"])
        self.send_by_id(id=user_id, msg=msg)
    
    def duxplorer(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["duxplorer"])
        self.send_by_id(id=user_id, msg=msg)

    def math(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["mathematical"])
        self.send_by_id(id=user_id, msg=msg)

    def eggseggs(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["eggseggs"])
        self.send_by_id(id=user_id, msg=msg)

    def latam(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["latam"])
        self.send_by_id(id=user_id, msg=msg)

    def fomo(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["fomo"])
        self.send_by_id(id=user_id, msg=msg)

    def mundo(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["mundo"])
        self.send_by_id(id=user_id, msg=msg)

    def eggpoint(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["eggpoint"])
        self.send_by_id(id=user_id, msg=msg)

    def endoworld(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["endoworld"])
        self.send_by_id(id=user_id, msg=msg)

    def marvinfavis(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["marvinfavis"])
        self.send_by_id(id=user_id, msg=msg)

    def eggmoon(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["eggmoon"])
        self.send_by_id(id=user_id, msg=msg)

    def duckstreet(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["duckstreet"])
        self.send_by_id(id=user_id, msg=msg)

    def kolkhoz(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["kolkhoz"])
        self.send_by_id(id=user_id, msg=msg)

    def forklog(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["forklog"])
        self.send_by_id(id=user_id, msg=msg)

    def cgu(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["cgu"])
        self.send_by_id(id=user_id, msg=msg)

    def insiders(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        msg = str(self.farms["insiders"])
        self.send_by_id(id=user_id, msg=msg)

    def check_address(self, address):
        res = "*Votes:*\n"
        key = f"VOTE_{address}_"
        for farm in self.farms.values():
            for el in farm.data:
                if key in el["key"]:
                    if el["value"] == "true":
                        res += f"-- *{farm.name} Liquidate: YES*\n"
                    if el["value"] == "false":
                        res += f"-- *{farm.name} Liquidate: NO*\n"
        return res

                
        

    ###############################################

    ############ HANDLERS #########
    # handle /start command. If user exists, send welcome message, else create user
    def start(self, update, context):
        """Handling start of user  communications with bot (/start)
        if new user, create and add entity to USER_MANAGER
        if existing user, send welcome message"""
        # print(update)
        name = update.message.chat.username
        user_id = update.message.chat.id
        if not self.check_id_fake(user_id):
            user = self.user_manager.create_user(user_id, name)
            # loglog(msg=f"User {id} {name} joined")
            msg = self.get_welcome_msg()
            self.send_by_id(id=user_id, msg=msg)
            if name != None:
                name = user.name.replace("_", "\_")
            else:
                name = "None"
            self.send_to_me(msg=f"User {user.id} {name} joined")

        else:
        # msg = f"Welcome! Your have {user.deposit} attempts. Enter /help to see available options"
            # self.send_to_me(msg=f"User {user.id} {user.name} joined")
            msg = self.get_welcome_msg()
            self.send_by_id(id=user_id, msg=msg)

    def add_new_user(self, user_id, name):
        self.calls += 1
        user = self.user_manager.create_user(user_id, name)
        if name != None:
            name = name.replace("_", "\_")
        else:
            name = "None"
        if not self.check_id_fake(user_id):
            # loglog(msg=f"User {id} {name} joined")
            self.send_to_me(msg=f"User {user.id} {name} joined, calls: {self.calls}")
        else:
            self.send_to_me(msg=f"User {user.id} {name}, calls: {self.calls}")

    def txt_handler(self, update, context):
        """Handle direct user input, whithout commands"""
        user_id = update.message.chat.id
        name = update.message.chat.username
        text = update.message.text
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        # self.user_manager.decrement_deposit(user_id=user_id)
        # self.send_by_id(id=id, msg="Sorry, paused for fixing, for approximately 2h, all deposits will be restored :)")
        # msg = self.parse_text(text)
        # msg = msg.replace("*", "\*")
        # msg = msg.replace("_", "\_")

        parse = self.parse_text(text)
        if parse != "None":
            self.send_by_id(id=user_id, msg=parse)

    def parse_text(self, text):
        """ Mentioned as main processing method
        Parse text, entered by user, check for correctness and call another methods
        accordingly to user input"""

        # result = "Your are so awesome :-), paste Waves address to check your votes"
        result = "None"
        matches = re.search(r"^[a-zA-Z0-9]+$", text)
        if matches:
            if len(text) == 35:
                votes = self.check_address(text)
                return f"*{text}:*\n{votes}"
        return result

    def address(self, update, context):
        user_id = update.message.chat.id
        name = update.message.chat.username
        self.add_new_user(user_id, name)
        if len(context.args) == 1:
            res = self.parse_text(context.args[0])
            if res != "None":
                msg = res
            else:
                msg = "Your are so awesome :-) But address is incorrect"
        else:
            msg = "Your are so awesome:) How to use: \n /address 3P8968LuSXboHgKi94PHvc6c17duA6i8Hw8"
        self.send_by_id(id=user_id, msg=msg)
    
    def depo(self, update, context):
        """Prints deposit amount for user, called this command"""
        user_id = update.message.chat.id
        user_depo = self.user_manager.get_user_deposit(user_id=user_id)
        self.send_by_id(id=user_id, msg=f"Your deposit is {user_depo}")

    def rset(self, update, context):
        """Service command which resets deposit to default value for user that called it
        JUST for testing purpose. Should be disabled for production use"""
        user_id = update.message.chat.id
        self.user_manager.set_deposit(user_id=user_id)
        user_depo = self.user_manager.get_user_deposit(user_id=user_id)
        self.send_by_id(id=user_id, msg=f"Your deposit is {user_depo}")

    def requestdepo(self, update, context):
        """Make record in deporequests.txt that user requested increasing its deposit
        Sends to administrator message about this
        User should place its address to identify if he made payment
        /requestdepo ADDRESS"""
        user_id = update.message.chat.id
        user = self.user_manager.get_user(user_id=user_id)
        if user != None:
            if len(context.args) == 1:
                address = context.args[0]
                if address.startswith("3P") and len(address) == 35:
                    self.user_manager.request_deposit(user_id=user_id, address=address)
                    self.send_by_id(id=user.id, msg=f"Request received, wait for confirm. Address: {address}")
                    self.send_to_me(msg=f"User {user.id} {user.name} requested deposit. Address: {address}")
                else:
                    self.send_by_id(id=user_id, msg="Invalid address")
            else:
                self.send_by_id(id=user_id, msg="Invalid params")

    def refill(self, update, context):
        """ Increase user deposit (attempts) by given value
        /refill USER_ID AMOUNT"""
        caller_id = update.message.chat.id
        if str(caller_id) == self.my_id:
            if len(context.args) == 2:
                try:
                    user_id = int(context.args[0])
                    depo = int(context.args[1])
                except ValueError:
                    self.send_by_id(id=caller_id, msg="Ivalid params")
                    return
                if self.user_manager.increment_deposit(user_id=user_id, amount=depo):
                    msg = f"Deposit incremented by {depo} for user {user_id}"
                    self.send_by_id(id=caller_id, msg=msg)
                    self.send_by_id(id=user_id, msg=f"Your deposit incremented by {depo}")
                else:
                    self.send_by_id(id=caller_id, msg=f"User {user_id} not found")
            else:
                self.send_by_id(id=caller_id, msg="Ivalid params")
        else:
            self.send_by_id(id=caller_id, msg="Your are not allowed for this command")

    def broadcast(self, update, context):
        """Send message, received from telegram to all users
        /broadcast MESSAGE"""
        caller_id = update.message.chat.id
        if str(caller_id) == self.my_id:
            if len(context.args) >= 1:
                msg = " ".join(context.args)
                msg = "INFO: " + msg
                self.send_to_all(msg=msg)
            else:
                self.send_to_me(msg="Invalid Params")

    def sendto(self, update, context):
        """Receive user ID and message from telegram, send
        /sendto USER_ID MESSAGE"""
        caller_id = update.message.chat.id
        if str(caller_id) == self.my_id:
            if len(context.args) >= 2:
                recip_id = int(context.args[0])
                txt = context.args[1:]
                msg = " ".join(txt)
                msg = "INFO: " + msg
                if self.check_id(user_id=caller_id):
                    self.send_by_id(id=recip_id, msg=msg)
                else:
                    self.send_to_me(msg=f"user id {recip_id} not found")
            else:
                self.send_to_me(msg="Invalid Params")

    def get_welcome_msg(self):
        l1 = f"Colllective Farm Liquidation Voting Info. Updated once in 10 minutes\n"
        main = f"*Paste address to see your votes*\n"
        # depo = f"/depo - to see your current deposit (attempts)\n"
        # donat = f"Donats are welcome: *3PPKpbjNRzsBicoSSNVP7suvmumrTsZP62J*"
        msg = f"{l1}{main}"
        return msg

    def help(self, update, context):
        id = update.message.chat.id
        user = self.user_manager.get_user(user_id=id)
        msg = self.get_welcome_msg()
        self.send_by_id(id=id, msg=msg)
        # loglog(f"{user.id} {user.name} called /help")




            



