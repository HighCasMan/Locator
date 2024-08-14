from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем модуль настроек Django по умолчанию для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')

# Загружаем конфигурацию из настроек проекта, используя пространство имен 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в файлах tasks.py в приложениях Django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
