from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN, OWNER_ID

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    mention = f"{user.first_name}"
    keyboard = [
        [
            InlineKeyboardButton("Source Code", url=f""),
            InlineKeyboardButton("Support Chat", url=f"")
        ],
        [
            InlineKeyboardButton("Add me to group", url=f"https://t.me/LiShiyaBot?startgroup=true")
        ],
        [
            InlineKeyboardButton("Owner Profile", url=f"https://t.me/{OWNER_ID}"),
        ]
    ]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo="")
    update.message.reply_text(f'Hello! {mention}! I am Edit Guardian bot I delete Edited message', reply_markup=InlineKeyboardMarkup(keyboard))

def check_edit(update: Update, context: CallbackContext):
    bot: Bot = context.bot

   
    if update.edited_message:
        edited_message = update.edited_message

        
        chat_id = edited_message.chat_id
        message_id = edited_message.message_id

        
        user_id = edited_message.from_user.id

        
        user_mention = f"{edited_message.from_user.first_name}"

            # Send a message notifying about the deletion
            bot.send_message(chat_id=chat_id, text=f"{user_mention} just edited a message🤡. I deleted his edited message🙂‍↕️🤡.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Start command handler
    dp.add_handler(CommandHandler("start", start))

    # Message edit handler
    dp.add_handler(MessageHandler(Filters.update.edited_message, check_edit))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()