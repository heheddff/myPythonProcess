# coding=gbk

import time

from .getpid import GetPid
from .checkpid import CheckPid
from .manager import Manager
from .log import Log
from .sendmail import Mail

class Core(object):
    # ��Ӫ������
    filename = "D:\\web_log\\login_gate\\runservers.ini"
    # filename = "group.ini"
    # ��������
    command = 'taskkill /F  /PID {}'
    # �����ļ�·��
    basepath = "D:\\pcik15\\pk15_dbc_for_dbview\\base-ver"
    # Ŀ��Ŀ¼
    dstpath = "D:\\pcik15\\pk15_dbc_for_dbview\\{}"
    # cfg�����ļ�
    cfgfile = "D:\\pcik15\\pk15_dbc_for_dbview\\{}\\cfg\\pcik_15_dbc.ini"
    # ��������·��
    exe_path = "D:\\pcik15\\pk15_dbc_for_dbview\\{}\\pcik_15_dbc_x86_singalsave.exe"
    # log��־
    log_path = "D:\\pcik15\\pk15_dbc_for_dbview\\{}\\log\\"

    # ��ǰʱ��
    current_time = int(time.time())

    def __init__(self):
        self.getpid = GetPid()

        self.checkpid = CheckPid(base_path=self.dstpath)  # ��ȡ����Ŀ�����,base_path = self.dstpath)
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
        pids = self.getpid.getPid()  # ��ȡserid����Ӧ����
        res = self.checkpid.run(pids)  # ɸѡ�쳣����
        serid_from_ini = self.getpid.getServerIdFromFile()
        for serid in serid_from_ini:
            if serid not in res:
                res[serid] = 2

        newitems = list(res.items())
        newitems.sort(key=lambda x: x[0], reverse=True)
        #self.mail.send(self.log.readlog())
        return dict(newitems)


    def main(self, serid, status):
        pids = self.getpid.getPid()  # ��ȡserid����Ӧ����
        pid_serid = pids.get(serid, False)

        if status == 1:
            if self.checkpid.checkdesDir(serid) != True:  # ʵ��δ����
                self.manager.create_new_ser(serid)

            if pid_serid == False:
                self.manager.start(serid)
            msg = "{} �����ѳɹ�����".format(serid)
            self.log.log(msg)
            result = self.run([serid])
        elif status == 2:
            msg = "{} �����ѹر�".format(serid)
            self.log.log(msg)
            result = self.manager.stop(pid_serid, serid)
        elif status == 3:
            if self.checkpid.checkdesDir(serid) != True:  # ʵ��δ����
                self.manager.create_new_ser(serid)
            self.manager.restart(pid_serid,serid)
            msg = "{} ����������".format(serid)
            self.log.log(msg)
            result = self.run([serid])

        self.mail.send(self.log.readlog())
        return result
