import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from difflib import get_close_matches

BOT_TOKEN = "7659284054:AAHFyNile7jBV_OY5NfZvIBw3Z-KhgGUG-k"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Basic GK questions
GK_QUESTIONS = {
    "who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "who is the president of india": "The President of India is Droupadi Murmu.",
    "what is the national animal of india": "The national animal of India is the Bengal Tiger.",
    "what is the national bird of india": "The national bird of India is the Indian Peacock.",
}

def find_best_match(question: str) -> str:
    question = question.lower().strip("?!. ")
    matches = get_close_matches(question, GK_QUESTIONS.keys(), n=1, cutoff=0.6)
    if matches:
        return GK_QUESTIONS[matches[0]]
    return "I'm not sure about that yet. Please ask a simple GK question!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi! I'm a GK Bot. Ask me a general knowledge question.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_question = update.message.text
    answer = find_best_match(user_question)
    await update.message.reply_text(answer)

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
