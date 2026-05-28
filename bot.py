import os
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("8917429307:AAHUKc2gM10y_eF968QI6FbzrApJtXJaLeQ")

async def start(update: Update, context):
    await update.message.reply_text("سلام! زه ستاسو بوټ یم.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("بوټ چلېږي...")
    app.run_polling()

if __name__ == "__main__":
    main()
