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
    print("5")


# if __name__ == "__main__":
#     text = "Привет"
#     chat_id = 302963265
#     send_message(
#         text=text, chat_id=chat_id
#     ) #пользователю 123456 ушло сообщение "Привет"
