#@RaveGen MessageHandler Filters.text
def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)