import time
from demo import app

@app.task
def add(x,y):
    time.sleep(4)
    return x+y