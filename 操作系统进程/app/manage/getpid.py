# coding=gbk

import psutil
import os


class GetPid(object):
    # ��Ӫ������
    filename = "D:\\web_log\\login_gate\\runservers.ini"

    # ����Ĭ�ϳ�����
    def __init__(self, pidname='pcik_15_dbc_x86_singalsave.exe'):
        self.pidname = pidname

    # ɸѡ��ָ������
    def getPid(self, des_serid=None):
        try:
            pids = psutil.pids()
            # print(pids)
            pidspath = {}

            for pid in pids:
                serverid = self.filterPid(pid)
                if serverid:
                    pidspath[serverid] = pidspath.get(serverid, []) + [pid]
            # print(pidspath)
            # ����ָ������
            pidspath = self.filterDesPid(des_serid, pidspath)
        # print(pidspath)
        except Exception as e:
            print(e)
            return False
        else:
            return pidspath

    # ����ָ������
    def filterDesPid(self, des_serid, src_serids):
        new_pidspath = {}
        try:
            if des_serid:
                print(des_serid)
                try:
                    for serid, pids in src_serids.items():
                        if serid in des_serid or serid == des_serid:
                            new_pidspath[serid] = pids
                except Exception as e:
                    print(e)
                    return False
                else:
                    return new_pidspath
            else:
                return src_serids
        except Exception as e:
            print(e)
            return src_serids

    # ɸѡ��ָ������
    def filterPid(self, pid):
        try:
            p = psutil.Process(pid)

            serverid = self.getPidId(p.cwd())
            # print(serverid)
            if self.pidname == p.name() and serverid:
                return serverid
        except Exception as e:
            # print(e)
            return False

    # ��ȡ��������Ŀ¼�ı��
    def getPidId(self, pidpath):
        return pidpath.split('\\')[-1] if os.path.exists(pidpath) else False

    # ��ʽ��serverid
    def getServerIdFromFile(self):
        data = self.getDataFromFile()

        if data:
            return set(filter(lambda x: x.strip(), data.split("\n")))
        else:
            return set()

    # ��ȡ�ļ�����Ӫ������id
    def getDataFromFile(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return f.read().strip('\n')
            except Exception as e:
                print(e)
                return False
        else:
            return False



