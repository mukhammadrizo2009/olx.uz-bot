import requests
from decouple import config
from telegram import Update
from telegram.ext import ContextTypes

ME_URL = config("ME_URL")

async def me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    access_token = context.user_data.get("access")

    if not access_token:
        await update.message.reply_text("❌ Avval /start bosing")
        return

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(ME_URL, headers=headers)

        if response.status_code == 200:
            user = response.json()

            text = f"""
👤 Profilingiz:

🪪ID: {user.get("id")}
〽️Username: {user.get("username")}
✨Ism: {user.get("first_name")}
⭐️Familiya: {user.get("last_name")}
"""
            await update.message.reply_text(text)

        else:
            await update.message.reply_text("❌ Profilingizni yuklab olib bo'lmadi!")

    except Exception:
        await update.message.reply_text("❌ Server bilan muammo yuzaga keldi tez orada bartaraf etiladi!")