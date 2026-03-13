import requests
from decouple import config
from telegram import Update
from telegram.ext import ContextTypes

LOGIN_URL = config("BACKEND_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    data = {
        "telegram_id": user.id,
        "username": user.username or "",
        "first_name": user.first_name or "",
        "last_name": user.last_name or "",
    }

    try:
        response = requests.post(LOGIN_URL, json=data)

        if response.status_code == 200:
            result = response.json()

            context.user_data["access"] = result.get("access")
            context.user_data["refresh"] = result.get("refresh")

            await update.message.reply_text(
                "✅ Siz muvaffaqiyatli tizimga kirdingiz yoki ro'yxatdan o'tdingiz!"
            )
        else:
            await update.message.reply_text("❌ Backend xatolik qaytardi")

    except Exception as e:
        await update.message.reply_text(f"❌ Server xatosi:\n{e}")