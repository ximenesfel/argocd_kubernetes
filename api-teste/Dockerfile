FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

COPY . /api
RUN pip3 install fastapi==0.90.1
RUN pip3 install uvicorn==0.20.0

WORKDIR /api

EXPOSE 5000

# Execution command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]