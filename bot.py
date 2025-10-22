import os
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes


BOT_TOKEN = os.environ.get("7704208492:AAFmCwy5rwTT3DOIkXMHD7AVk_PxgOjmpds")  

async def approve_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Автоматически одобряет любую заявку на вступление в канал или группу.
    """
    user = update.chat_join_request.from_user
    chat = update.chat_join_request.chat

    try:
        # Одобряем заявку
        await update.chat_join_request.approve()
        print(f"Заявка от пользователя {user.first_name} (id: {user.id}) одобрена в чате '{chat.title}'")
        
        # Опционально: отправляем приветственное сообщение пользователю
        # try:
        #     await context.bot.send_message(
        #         chat_id=user.id,
        #         text="Ваша заявка одобрена! Добро пожаловать в наш канал!"
        #     )
        # except Exception as e:
        #     print(f"Не удалось отправить сообщение пользователю {user.id}: {e}")

    except Exception as e:
        print(f"Ошибка при одобрении заявки от {user.id}: {e}")

def main():
    # Создаем приложение и передаем ему токен бота
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчик заявок на вступление
    application.add_handler(ChatJoinRequestHandler(approve_join_request))

    # Запускаем бота в режиме опроса (polling)
    print("Бот запущен...")
    application.run_polling()

if name == "__main__":
    main()
