from bot_comands import *

# if __name__ == "main":
app = ApplicationBuilder().token("5759772520:AAEVHcs8e7Jd4lA-pjZ8GoZRcZR382rCnWs").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("get", get_command))
app.run_polling()