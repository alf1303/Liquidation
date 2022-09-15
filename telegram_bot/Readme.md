Telegram Bot Utility, using python-telegram-bot (https://pypi.org/project/python-telegram-bot/)

It is used for simplified adding to projects ability to send messages receive commands to/from telegram bot.
Also it contains very basic UserManager module, for managing users.

Usage:
- Copy telegram_bot folder to you project directory
- Import:
    from telegram_bot.telegram_bot import MyBot
- Init:
    telegram_bot_token = "6666666666:AAH1UxdJSoOxJqs_4WwffgKaSgb9ptgriRs"
    bot = MyBot(token=telegram_bot_token, default_deposit=15)
