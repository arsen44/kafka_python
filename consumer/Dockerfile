FROM python:3.11-slim-buster

# Устанавливаем переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости для confluent-kafka
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    librdkafka-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем основной скрипт
ADD main.py /app/main.py

# Указываем точку входа
ENTRYPOINT ["python3", "/app/main.py"]
CMD ["--topic", "hello_topic", "--kafka", "kafka:9092"]

