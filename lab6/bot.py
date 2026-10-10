import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

load_dotenv(override=True)

# Три состояния конечного автомата
CHOOSE_DRINK, CHOOSE_SIZE, CONFIRM = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["☕ Эспрессо", "☕ Американо"],
        ["🥛 Капучино", "🍶 Латте"],
        ["🥤 Раф"]
    ]

    await update.message.reply_text(
        "Добро пожаловать в Coffee Bot! ☕\n"
        "Выберите напиток:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

    return CHOOSE_DRINK


async def choose_drink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    drink = update.message.text
    context.user_data["drink"] = drink

    keyboard = [
        ["Маленький", "Средний"],
        ["Большой"]
    ]

    await update.message.reply_text(
        "Теперь выберите размер:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

    return CHOOSE_SIZE


async def choose_size(update: Update, context: ContextTypes.DEFAULT_TYPE):
    size = update.message.text
    context.user_data["size"] = size

    drink = context.user_data["drink"]

    keyboard = [
        ["✅ Подтвердить", "❌ Отмена"]
    ]

    await update.message.reply_text(
        f"Ваш заказ:\n"
        f"Напиток: {drink}\n"
        f"Размер: {size}\n\n"
        f"Подтвердить заказ?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

    return CONFIRM


async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    drink = context.user_data["drink"]
    size = context.user_data["size"]

    await update.message.reply_text(
        f"✅ Заказ подтверждён!\n"
        f"{drink}, размер: {size}.\n"
        f"Спасибо за заказ!",
        reply_markup=ReplyKeyboardRemove()
    )

    context.user_data.clear()

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "❌ Заказ отменён.",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print("Ошибка: токен не найден в файле .env")
        return

    app = ApplicationBuilder().token(token).build()

    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start)
        ],

        states={
            CHOOSE_DRINK: [
                MessageHandler(
                    filters.Regex(
                        "^(☕ Эспрессо|☕ Американо|🥛 Капучино|🍶 Латте|🥤 Раф)$"
                    ),
                    choose_drink
                )
            ],

            CHOOSE_SIZE: [
                MessageHandler(
                    filters.Regex(
                        "^(Маленький|Средний|Большой)$"
                    ),
                    choose_size
                )
            ],

            CONFIRM: [
                MessageHandler(
                    filters.Regex("^✅ Подтвердить$"),
                    confirm
                ),
                MessageHandler(
                    filters.Regex("^❌ Отмена$"),
                    cancel
                )
            ]
        },

        fallbacks=[
            CommandHandler("start", start)
        ],

        allow_reentry=True
    )

    app.add_handler(conversation_handler)

    print("Coffee Bot запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()