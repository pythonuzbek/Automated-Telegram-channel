import os

from telebot import TeleBot

from dotenv import load_dotenv
load_dotenv()

bot = TeleBot(
    token=os.getenv('BOT_TOKEN'),
    parse_mode='html',
    disable_web_page_preview=True,
)

chat_id = os.getenv('CHANNEL_ID')

if __name__ == '__main__':
    bot.send_message(
        chat_id=chat_id,
        text='Diyor qalaysan ?',
    )