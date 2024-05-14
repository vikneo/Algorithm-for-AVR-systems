import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_avr.settings')

app = Celery('system_avr')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()