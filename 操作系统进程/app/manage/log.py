import time
import os


class Log(object):
    # 记录操作日志
    logname = 'log\\' + time.strftime("%Y-%m-%d", time.localtime()) + '_manageserver.txt'

    def __init__(self):
        if os.path.exists('log') == False:
            os.mkdir('log')

    @classmethod
    def log(cls, msg):
        msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '	' + msg + "\n"
        with open(cls.logname, 'a+') as f:
            f.write(msg)

    @classmethod
    def readlog(cls):
        with open(cls.logname) as f:
            return f.read()
