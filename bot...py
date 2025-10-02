from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот. Введи выражение, и я его посчитаю.")

app = ApplicationBuilder().token("ВАШ_ТОКЕН_БОТА").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
