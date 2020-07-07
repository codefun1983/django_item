import os
from celery import Celery
from youtube_download.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_download.settings')	#setting activate to environment
app = Celery('app',broker=CELERY_BROKER_URL)							#create celery task
app.config_from_object('django.conf:settings', namespace='CELERY')	#recieve setting information from celery
app.autodiscover_tasks()	#auto loading task

@app.task(bind=True)
def debug_task(self):
   print('Request: {0!r}'.format(self.request))