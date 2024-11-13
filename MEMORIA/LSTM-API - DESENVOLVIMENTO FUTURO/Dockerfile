FROM python:3.8-slim

WORKDIR /app

COPY ./app /app
COPY ./models /models
COPY ./data /data

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
