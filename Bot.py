from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Olá! Bem-vindo ao bot de cobrança.")

async def responder(update: Update, context: CallbackContext):
    await update.message.reply_text("Este é um bot de cobrança. Aguarde novidades!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

if __name__ == "__main__":
    print("Bot está rodando...")
    app.run_polling()
