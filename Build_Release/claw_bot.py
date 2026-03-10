import subprocess
import os
import platform
import time
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8722167197:AAEC482AW_VLAPipXxHOxgkfnk3ydfrjcg4"

keyboard = [["▶ PLAY"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏴‍☠️ Captain Claw бот готов.\nНажми кнопку чтобы запустить игру.",
        reply_markup=markup
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subprocess.Popen(["/Users/ivanbulatov/OpenClaw/Build_Release/openclaw"])
    await update.message.reply_text("🎮 Запускаю Captain Claw!")
async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):

    uptime = subprocess.check_output(["uptime"]).decode().strip()
    hostname = platform.node()
    python_version = platform.python_version()

    message = (
        "🟢 Bot running\n\n"
        f"Host: {hostname}\n"
        f"Python: {python_version}\n"
        f"System uptime:\n{uptime}"
    )

    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("health", health))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("▶ PLAY"), play))

app.run_polling()
