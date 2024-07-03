FROM python:3.9.0-alpine3.12
RUN apk --no-cache add curl
EXPOSE 8000/tcp
CMD ["python", "-m", "http.server", "8000"]
