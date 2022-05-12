# # yourvenv/cfehome/celery.py
# from __future__ import absolute_import, unicode_literals # for python2
# from django.conf import settings
# import os
# from celery import Celery

# # set the default Django settings module for the 'celery' program.
# # this is also used in manage.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'omnichannel.settings')


# ## Get the base REDIS URL, default to redis' default
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

# app = Celery('omnichannel')

# # Using a string here means the worker don't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.broker_url = BASE_REDIS_URL





import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'omnichannel.settings')

app = Celery('omnichannel')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')