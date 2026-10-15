# Импорт необходимых библиотек
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

# Загружаем токен из файла .env
load_dotenv(override=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаём кнопки с жанрами фильмов
    keyboard = [
        ["😂 Комедия", "🚀 Фантастика"],
        ["🎭 Драма", "ℹ️ О боте"]
    ]

    # Настраиваем клавиатуру
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    # Отправляем приветствие и показываем кнопки
    await update.message.reply_text(
        "Привет! Я Movie Bot 🎬\nВыбери жанр фильма:",
        reply_markup=reply_markup
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем текст сообщения пользователя
    text = update.message.text

    # Проверяем выбранный жанр и отправляем рекомендацию

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

    # Показываем информацию о боте
    elif text == "ℹ️ О боте":
        await update.message.reply_text(
            "Movie Bot — простой Telegram-бот на Python, "
            "который рекомендует фильмы по жанру."
        )

    # Ответ на неизвестное сообщение
    else:
        await update.message.reply_text(
            "Пожалуйста, выбери жанр с помощью кнопок."
        )


def main():
    # Получаем токен бота
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    # Проверяем, найден ли токен
    if not token:
        print("Ошибка: токен не найден в файле .env")
        return

    # Создаём приложение бота
    app = ApplicationBuilder().token(token).build()

    # Регистрируем команду /start
    app.add_handler(
        CommandHandler("start", start)
    )

    # Регистрируем обработчик обычных текстовых сообщений
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("Movie Bot запущен...")

    # Запускаем бота
    app.run_polling()


# Запуск программы
if __name__ == "__main__":
    main()