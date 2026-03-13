from telegram.ext import ApplicationBuilder, CommandHandler
from decouple import config

from me_profile import me
from tokens import access, refresh
from start import start


BOT_TOKEN = config("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()



app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("access", access))
app.add_handler(CommandHandler("refresh", refresh))
app.add_handler(CommandHandler("me", me))

app.run_polling()