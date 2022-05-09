FROM python:alpine3.15

WORKDIR /app
RUN pip install --no-cache-dir docker

COPY . /app

CMD ["python", "main.py"]