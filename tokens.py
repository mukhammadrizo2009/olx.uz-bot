from telegram import Update
from telegram.ext import ContextTypes


async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = context.user_data.get("access")

    if token:
        await update.message.reply_text(f"🔑 Access tokeningiz:\n{token}")
    else:
        await update.message.reply_text("❌ Bu amallar bajarish uchun avval /start bosing")


async def refresh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = context.user_data.get("refresh")

    if token:
        await update.message.reply_text(f"🔄 Refresh tokeningiz:\n{token}")
    else:
        await update.message.reply_text("❌ Bu amallar bajarish uchun avval /start bosing")