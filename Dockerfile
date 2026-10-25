FROM python:3.14-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade \
    "msgpack>=1.2.1" \
    "setuptools>=78.1.1" \
    "urllib3>=2.8.0" \
    -r requirements.txt
COPY . .

ENV PORT=8080
EXPOSE 8080
USER 1000:1000
CMD ["python3", "src/server.py"]
