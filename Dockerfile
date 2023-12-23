FROM python:3.9-alpine

WORKDIR / Locator

ENV PYTHONDONTWRITECODE = 1
ENV PYTHONUNBUFFERED = 1

WORKDIR /usr/src/Locator

COPY . .



RUN pip install -r /Locator

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]