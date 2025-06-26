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

# GK FAQ database
GK_QUESTIONS = {
    "prime minister of india": "🇮🇳 The Prime Minister of India is Narendra Modi.",
    "president of india": "🇮🇳 The President of India is Droupadi Murmu.",
    "capital of france": "🇫🇷 The capital of France is Paris.",
    "tallest mountain": "🏔️ Mount Everest is the tallest mountain in the world.",
    "largest ocean": "🌊 The Pacific Ocean is the largest in the world.",
    "capital of india": "The capital of India is New Delhi.",
    "national animal of india": "The national animal of India is the Bengal Tiger.",
    "national bird of india": "The national bird of India is the Indian Peacock.",
}

def get_best_match(user_text):
    question = user_text.lower().strip("?!. ")
    best_match = get_close_matches(question, GK_QUESTIONS.keys(), n=1, cutoff=0.5)
    if best_match:
        return GK_QUESTIONS[best_match[0]]
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Welcome to GK Bot! Ask me any general knowledge question.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    answer = get_best_match(user_question)
    if answer:
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("🤔 I'm not sure about that yet. Please ask a simple GK question!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ GK Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
