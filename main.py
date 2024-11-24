from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton, ChatMember
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN, OWNER_ID

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    mention = f"{user.first_name}"
    keyboard = [
        [
            InlineKeyboardButton("NETWORK", url=f"https://t.me/Kayto_Official"),
            InlineKeyboardButton("SUPPORT CHAT", url=f"https://t.me/Anime_Chat_Group_Community")
        ],
        [
            InlineKeyboardButton("ADD ME", url=f"https://t.me/KaytoGuardian_bot?startgroup=true")
        ],
        [
            InlineKeyboardButton("STARBOY", url=f"https://t.me/Username_Of_Tuhin"),
        ]
    ]

    context.bot.send_photo(chat_id=update.effective_chat.id, photo="https://envs.sh/K0_.jpg")
    update.message.reply_text(
        f"⛩️ Hello {mention}!❖ I'm Kayto Guardian. I delete edited messages in groups to maintain transparency.📡 You'll be notified each time a message is deleted ✦ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғᴏʀ ᴍᴀɪɴᴛᴀɪɴ sᴇᴄᴜʀɪᴛʏ.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

def check_edit(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    edited_message = update.edited_message
    if not edited_message:
        return  # Ignore if no edited message

    chat_id = edited_message.chat_id
    message_id = edited_message.message_id
    user_id = edited_message.from_user.id
    user_mention = f"{edited_message.from_user.first_name}"

    # Check if the user is the owner
    if user_id == OWNER_ID:
        return  # Ignore if the owner edits the message

    # Check if the user is an admin
    member = bot.get_chat_member(chat_id, user_id)
    if member.status in [ChatMember.ADMINISTRATOR, ChatMember.CREATOR]:
        return  # Ignore if the user is an admin or creator (owner)

    # Notify and delete the edited message
    bot.send_message(chat_id=chat_id, text=f"{user_mention} just edited a message🤡. I deleted their edited message🙂‍↕️🤡.")
    bot.delete_message(chat_id=chat_id, message_id=message_id)

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
