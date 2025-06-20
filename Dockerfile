FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    build-essential \
    libmariadb-dev-compat \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8080

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]