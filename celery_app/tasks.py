
from . import celery
import time




@celery.task(bind=True)
def celery_task(self):
    print("celery_app.task start")
    time.sleep(5)
    print("celery_app.task end")
    return True