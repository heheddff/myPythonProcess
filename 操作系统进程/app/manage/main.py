# coding=gbk

import time

from .getpid import GetPid
from .checkpid import CheckPid
from .manager import Manager
from .log import Log
from .sendmail import Mail

class Core(object):
    # 运营服务器
    filename = "D:\\web_log\\login_gate\\runservers.ini"
    # filename = "group.ini"
    # 结束进程
    command = 'taskkill /F  /PID {}'
    # 基本文件路径
    basepath = "D:\\pcik15\\pk15_dbc_for_dbview\\base-ver"
    # 目标目录
    dstpath = "D:\\pcik15\\pk15_dbc_for_dbview\\{}"
    # cfg配置文件
    cfgfile = "D:\\pcik15\\pk15_dbc_for_dbview\\{}\\cfg\\pcik_15_dbc.ini"
    # 启动程序路径
    exe_path = "D:\\pcik15\\pk15_dbc_for_dbview\\{}\\pcik_15_dbc_x86_singalsave.exe"
    # log日志
    log_path = "D:\\pcik15\\pk15_dbc_for_dbview\\{}\\log\\"

    # 当前时间
    current_time = int(time.time())

    def __init__(self):
        self.getpid = GetPid()

        self.checkpid = CheckPid(base_path=self.dstpath)  # 获取所有目标进程,base_path = self.dstpath)
        self.manager = Manager(self.basepath, self.dstpath, self.exe_path, self.cfgfile)
        self.log = Log()
        self.mail = Mail()

    def run(self, res):
        i = 1
        #print(res)
        while len(res) > 0:
            time.sleep(1)
            check_run = self.checkpid.run(res,self.current_time)
            if check_run[res[0]] == 1:
                return check_run
            print(check_run)
            if i > 15:
                break
            i += 1
        return check_run

    def init_serid(self):
        pids = self.getpid.getPid()  # 获取serid及对应进程
        res = self.checkpid.run(pids)  # 筛选异常进程
        serid_from_ini = self.getpid.getServerIdFromFile()
        for serid in serid_from_ini:
            if serid not in res:
                res[serid] = 2

        newitems = list(res.items())
        newitems.sort(key=lambda x: x[0], reverse=True)
        #self.mail.send(self.log.readlog())
        return dict(newitems)


    def main(self, serid, status):
        pids = self.getpid.getPid()  # 获取serid及对应进程
        pid_serid = pids.get(serid, False)

        if status == 1:
            if self.checkpid.checkdesDir(serid) != True:  # 实例未创建
                self.manager.create_new_ser(serid)

            if pid_serid == False:
                self.manager.start(serid)
            msg = "{} 服务已成功启动".format(serid)
            self.log.log(msg)
            result = self.run([serid])
        elif status == 2:
            msg = "{} 服务已关闭".format(serid)
            self.log.log(msg)
            result = self.manager.stop(pid_serid, serid)
        elif status == 3:
            if self.checkpid.checkdesDir(serid) != True:  # 实例未创建
                self.manager.create_new_ser(serid)
            self.manager.restart(pid_serid,serid)
            msg = "{} 服务已重启".format(serid)
            self.log.log(msg)
            result = self.run([serid])

        self.mail.send(self.log.readlog())
        return result
