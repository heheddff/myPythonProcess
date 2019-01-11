from myplatform import celery_app as app
import time
@app.task
def func():
    time.sleep(6)
    return 2+3