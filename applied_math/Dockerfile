# Установка базового образа
FROM python:3.11-bullseye

# Установка переменной окружения PYTHONUNBUFFERED в значение 1,
# чтобы вывод команд Python был сразу доступен в консоли
ENV PYTHONUNBUFFERED=1

# Создание рабочей директории внутри контейнера
WORKDIR /usr/src/tsuab/applied_math

# Копирование requirements.txt в контейнер
COPY requirements.txt .

# Установка зависимостей проекта
RUN pip install -r requirements.txt
# Копирование всего содержимого проекта в контейнер
COPY . /usr/src/tsuab/applied_math

RUN python manage.py collectstatic --no-input


EXPOSE 8000

# Команда для запуска сервера Django
CMD python manage.py runserver 0.0.0.0:8000