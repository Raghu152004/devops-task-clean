FROM python:3.12-slim

WORKDIR /app

COPY environment/ /app

RUN pip install --no-cache-dir pytest==7.4.0

CMD ["python", "main.py"]