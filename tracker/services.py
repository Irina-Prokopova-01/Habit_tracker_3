import requests

from config import settings


def send_message(text, chat_id):
    """Функция отправки сообщений через телеграм-бот.
    Принимает текст сообщения и id чата, отправляет его."""
    params = {
        "text": text,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage", params=params
    )


# if __name__ == "__main__":
# text = "Test message"
# chat_id = 123456
# send_message(
#     text=text, chat_id=chat_id
# ) пользователю 123456 ушло сообщение "Привет"
