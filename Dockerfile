FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
ARG APP_VERSION=v1
ENV APP_VERSION=$APP_VERSION
CMD ["python", "app.py"]
