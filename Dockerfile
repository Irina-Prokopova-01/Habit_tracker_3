# Указываем базовый образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /habit_tracker_3

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root

COPY . .

RUN mkdir -p /habit_tracker_3/staticfiles && chmod -R 755 /habit_tracker_3/staticfiles

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
