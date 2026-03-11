import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("8611289628:AAFcPtzIiESg_oCFHga-FnIm1bGRHcFOU2M")
print("TOKEN FROM ENV:", TOKEN)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Бот онлайн ✅")


async def health(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("OK")


def main() -> None:
    if not TOKEN:
        if not TOKEN:
    print("WARNING: BOT_TOKEN не найден")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("health", health))

    print("Bot started")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()