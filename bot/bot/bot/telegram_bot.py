from telegram import Bot, ParseMode

TOKEN = "8036950118:AAHTspZbfB6pyvtTMBpW6wLHHX3DTAuM_eg"
CHAT_ID = "-1002808462256"
bot = Bot(token=TOKEN)

def send_signal(message):
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)

def delete_message(msg_id):
    try:
        bot.delete_message(chat_id=CHAT_ID, message_id=msg_id)
    except:
        pass
