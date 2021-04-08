import os
import logging
from get_page import check_result
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(level=logging.DEBUG)

def start(update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Starting...")

    context.job_queue.run_repeating(callback=send_projects, interval=300, first=20, context=update)

def send_projects(context):

    print("Looking for new projects")

    results = check_result()
    print(results)

    if results == None:
        ...
    else:
        context.bot.send_message(chat_id=391999910, text=f"{results['title']}: {results['link']}")


def main_function():
    load_dotenv()
    token = os.getenv('TOKEN')

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start, pass_job_queue=True)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main_function()