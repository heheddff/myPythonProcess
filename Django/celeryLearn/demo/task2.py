import time
from demo import app

@app.task
def multiply(x,y):
    time.sleep(4)
    return x*y


