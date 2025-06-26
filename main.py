import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import difflib

BOT_TOKEN = "7659284054:AAHFyNile7jBV_OY5NfZvIBw3Z-KhgGUG-k"

logging.basicConfig(level=logging.INFO)

faq_data = {
    "prime minister of india": "🇮🇳 The Prime Minister of India is Narendra Modi.",
    "president of india": "🇮🇳 The President of India is Droupadi Murmu.",
    "capital of france": "🇫🇷 The capital of France is Paris.",
    "tallest mountain": "🏔️ Mount Everest is the tallest mountain in the world.",
    "largest ocean": "🌊 The Pacific Ocean is the largest in the world.",
}

def get_best_match(user_text):
    best_match = difflib.get_close_matches(user_text, faq_data.keys(), n=1, cutoff=0.5)
    if best_match:
        return faq_data[best_match[0]]
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Welcome to GK Bot! Ask me any general knowledge question.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text.lower()
    response = get_best_match(user_question)
    if response:
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("🤔 I'm not sure about that yet. Please ask a simple GK question!")

# ✅ For Windows: no asyncio.run()
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ GK Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
