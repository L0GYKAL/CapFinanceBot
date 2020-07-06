# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:41:10 2020

@author: L0GYKAL
"""

import time
from pycoingecko import CoinGeckoAPI
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.parsemode import ParseMode
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


last_updated_at  = 0

cg = CoinGeckoAPI()

updater = Updater(token = "",
                  use_context=True)

dispatcher: Dispatcher = updater.dispatcher

def getPrice(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    print("carapuce")
    bot: Bot = context.bot
    global last_updated_at
    
    if last_updated_at < time.time()+2:
        data = cg.get_token_price(id = 'ethereum', contract_addresses = '0x43044f861ec040db59a7e324c40507addb673142', vs_currencies = 'usd', include_market_cap = 'true', include_24hr_vol = 'true', include_24hr_change = 'true', include_last_updated_at='true')['0x43044f861ec040db59a7e324c40507addb673142']
        last_updated_at = data['last_updated_at']
        response  = bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "Hello User, You have used price command d;).\n USD: $" + str(data['usd']) + " \n 24h change: " + str(data['usd_24h_change']) + "%  \n 24h volume of: $" + str(data['usd_24h_vol'])
        )
        print(response)
    

    # Added HTML Parser to the existing command handler
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.parsemode.html#telegram.ParseMode.HTML
    
dispatcher.add_handler(CommandHandler("cap", getPrice))

updater.start_polling()
