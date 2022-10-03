from bot_comands import *
from config import *


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("get", get_command))
app.add_handler(CommandHandler("download", download_command))
app.run_polling()
