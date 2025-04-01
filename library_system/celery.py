import os
from celery import Celery
from celery.beat import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'check_overdue_loans': {
        'task': 'library.tasks.check_overdue_loans',
        'schedule': crontab(minute=1, hour=1)
    }
}

app.autodiscover_tasks()
