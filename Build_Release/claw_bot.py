import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

print("BOT_TOKEN:", TOKEN)

if not TOKEN:
    print("WARNING: BOT_TOKEN не найден")

app = Application.builder().token(TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Бот онлайн ✅")


async def health(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("OK")


git add Build_Release/claw_bot.py
git commit -m "fix indentation"
git push origin main