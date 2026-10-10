import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv(override=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["😂 Комедия", "🚀 Фантастика"],
        ["🎭 Драма", "ℹ️ О боте"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Привет! Я Movie Bot 🎬\nВыбери жанр фильма:",
        reply_markup=reply_markup
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "😂 Комедия":
        await update.message.reply_text(
            "Рекомендую: «1+1» 🎬"
        )

    elif text == "🚀 Фантастика":
        await update.message.reply_text(
            "Рекомендую: «Интерстеллар» 🚀"
        )

    elif text == "🎭 Драма":
        await update.message.reply_text(
            "Рекомендую: «Зелёная миля» 🎭"
        )

    elif text == "ℹ️ О боте":
        await update.message.reply_text(
            "Movie Bot — простой Telegram-бот на Python, "
            "который рекомендует фильмы по жанру."
        )

    else:
        await update.message.reply_text(
            "Пожалуйста, выбери жанр с помощью кнопок."
        )


def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print("Ошибка: токен не найден в файле .env")
        return

    app = ApplicationBuilder().token(token).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("Movie Bot запущен...")

    app.run_polling()


if __name__ == "__main__":
    main()