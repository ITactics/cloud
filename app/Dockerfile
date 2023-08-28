# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и приложение
COPY requirements.txt .
COPY app.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, на котором будет слушать приложение
EXPOSE 8000

# Запускаем приложение при запуске контейнера
CMD ["python", "app.py"]
