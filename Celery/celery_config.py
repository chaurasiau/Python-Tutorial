from celery import Celery

# app = Celery('simple_with_celery', broker='redis://localhost:6379/0',
#              include=['simple_with_celery', 'celery_add'])

app = Celery('simple_with_config', broker='redis://localhost:6379/0',
             include=['packs.celery_fetch'])
