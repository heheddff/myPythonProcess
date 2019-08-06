# coding=gbk

import os
import re
from .log import Log


class CheckPid(object):
    checkres = {}

    def __init__(self, base_path='.\\'):
        self.base_path = base_path

    # self.serids = self.getSerid(pids)

    def check_logname(self, serid):
        log_paths = self.checklogDir(serid)
        log_names = self.getLastLog(log_paths)
        if log_names == False:
            return
        filter_log_paths = list(filter(self.matchLogType, log_names))
        return os.path.join(log_paths, filter_log_paths[-1]) if len(filter_log_paths) > 0 else False

    def get_log_time(self,log_name):
        return int(os.path.getctime(log_name))


    def getSerid(self, pids):
        return pids

    # return list(pids.keys()) if pids else False

    def checkdesDir(self, serid):
        dst_path = self.base_path.format(serid)
        # print(dst_path)
        if self.is_dir(dst_path):
            if len(os.listdir(dst_path)) > 0:
                # print('is not empty {}'.format(dst_path))
                return True
            else:
                os.rmdir(dst_path)
                return False
        else:
            return False

    def is_dir(self, dirpath):
        return os.path.isdir(dirpath)

    def checklogDir(self, serid):
        log_path = self.base_path.format(serid) + "\\log"
        return log_path if self.is_dir(log_path) else False

    def getLastLog(self, log_paths=None):
        return os.listdir(log_paths) if log_paths else log_paths

    # print(dirs)

    # 匹配日志格式
    def matchLogType(self, logname):
        log_type = r"\d{8}_\d{6}.log"
        # print(re.match(log_type,logname))
        return True if re.match(log_type, logname) else False

    def readlog(self, logname):
        if self.isexists(logname):
            with open(logname) as f:
                return f.read()
        else:
            return False

    # 判断日志路径是否正确
    def isexists(self, filename):
        return os.path.exists(filename)

    # 匹配日志内容
    def matchServerStatus(self, contents):
        pattern = r".*DBCache listen for game server at.*"
        #print(pattern)
        #print(contents)
        res = re.search(pattern, contents)
        #print(res)
        return res  # None表示未成功连接DB，需重启

    def check_status(self, logname):
        return self.matchServerStatus(self.readlog(logname)) if logname else None

    def run(self, pids=None,current_time=None):

        serids = pids
        checkres = {}

        for serid in serids:
            logname = self.check_logname(serid)
            if logname == False:
                checkres[serid] = 3
                msg = "{} 缺少日志文件".format(serid)
                Log.log(msg)
                continue

            if current_time != None and current_time > self.get_log_time(logname):
                checkres[serid] = 3
                msg = "{} 未生成新日志文件".format(serid)
                Log.log(msg)
                continue

            if self.check_status(logname) == None:
                    checkres[serid] = 3
                    msg = "{} 监听失败".format(serid)
                    Log.log(msg)
                    continue

            checkres[serid] = 1
        return checkres

    def runcheck(self, pids=None):

        serids = pids  # if pids else self.serids
        checkres = {}
        for serid in serids:
            logname = self.check_logname(serid)

            if logname == False:
                #self.add_serid(serid,3)
                checkres[serid] = 3
            else:
                if self.check_status(logname) == None:
                    #self.add_serid(serid,3)
                    checkres[serid] = 3
                else:
                    #self.del_serid(serid)
                    #self.add_serid(serid, 1)
                    checkres[serid] = 1
        return checkres

    def add_serid(self, serid,status):
        self.checkres[serid] = status

    def del_serid(self, serid):
        if serid in self.checkres:
            self.checkres.remove(serid)


