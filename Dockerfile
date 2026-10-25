FROM alpine:3.24

RUN apk add --no-cache python3

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY src/ ./src/

ENV PORT=8080
EXPOSE 8080

USER 1000:1000

CMD ["python3", "src/server.py"]
