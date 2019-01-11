import time
from tasks import add

if __name__ == '__main__':
    print('start task...')
    res = add.delay(4,8)
    print('end task...')
    print(res)