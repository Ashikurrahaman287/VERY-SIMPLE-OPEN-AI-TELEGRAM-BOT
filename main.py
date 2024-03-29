import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import openai

# Set up OpenAI API
openai_api_key = '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'
openai_base_url = 'https://api.openai.com/v1/'

# Set up Telegram Bot
bot_token = '6950405932:AAFxhK5znmbXQ4tPw5vhuIQhz-HhQgq-HJ8'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Define a function to handle user messages
def message_handler(update, context):
    user_input = update.message.text
    # Call OpenAI API to generate response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50
    )
    generated_text = response.choices[0].text.strip()
    # Send the generated response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text)

# Define a command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm SPUD AI bot. You can start chatting with me!")

# Set up handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
