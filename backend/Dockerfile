FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/app

RUN python3 manage.py migrate

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
