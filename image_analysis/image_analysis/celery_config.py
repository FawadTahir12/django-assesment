import os
from celery import Celery

from .settings.base import DEBUG


if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_analysis.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_analysis.settings.production')

celery_app = Celery('image_analysis')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
