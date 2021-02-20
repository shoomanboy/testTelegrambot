from telegram import bot, ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, Filters, MessageHandler, ConversationHandler, CommandHandler


def message_handler(bot,update):
    name=bot.message.chat.first_name
    bot.message.reply_text(text="Привет %s я бот"%name)
    # return ConversationHandler.END


def kek_handler(bot,update):
    bot.message.reply_text(text="конец")
    return ConversationHandler.END


def main():
    print("Бот запущен")
    updater=Updater(token="1626047788:AAHIne5kUY_koi6PMioBun5edTwrir87VLM",use_context=True)
    start_handler=updater.dispatcher.add_handler(CommandHandler("start",message_handler))
    end_handler = updater.dispatcher.add_handler(MessageHandler(Filters.regex("end"), kek_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()