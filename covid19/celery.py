from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covid19.settings')

app = Celery('covid19')
app.conf.timezone = 'UTC'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()