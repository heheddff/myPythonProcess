# coding=gbk

from shutil import copytree, rmtree
import os
import re


class Manager(object):
    command = 'taskkill /F  /PID {}'

    def __init__(self, base_dir, dst_path, exe_path, config_path):
        self.base_dir = base_dir
        self.exe_path = exe_path
        self.config_path = config_path
        self.dst_path = dst_path

    # print(self.base_dir)
    # print(self.exe_path)
    # print(self.config_path)

    def create_new_ser(self, serid):
        dst = self.dst_path.format(serid)
        # print(dst)
        try:
            copytree(self.base_dir, dst)
        except Exception as e:
            print(e)
            pass
        else:
            self.changeGameIni(serid)

    # 根据server id更改配置文件内容
    def changeGameIni(self, serid):
        path = self.config_path.format(serid)
        self.writeIni(self.defineRe(self.readIni(path), serid), path)

    # 替换文件制定内容
    def defineRe(self, txt, serid):
        try:
            txt = re.sub(r'port=2\d+', 'port=2' + str(serid), txt)
            txt = re.sub(r'groupid=\d+', 'groupid=' + str(serid), txt)
        except Exception as e:
            print(e)
        else:
            return txt

    # 读取配置文件内容
    def readIni(self, path):
        try:
            with open(path, 'r') as f:
                txt = f.read()
                f.close()
        except Exception as e:
            print(e)
        else:
            return txt

    # 保存替换后的内容
    def writeIni(self, content, path):
        try:
            with open(path, 'w') as f:
                f.write(content)
                f.close()
        except Exception as e:
            print(e)

    def start(self, serid):
        if len(serid) > 0:
            exe_path = self.exe_path.format(serid)
            # print(exe_path)
            os.startfile(exe_path)
        # self.log(msg='start '+exe_path)

    def stop(self, pids,serid):
        try:
            if pids and len(pids) > 0:
                for pid in pids:
                    print('成功结束进程:{}'.format(pid))
                    os.system(self.command.format(pid))
                # self.log(msg='shutdown '+'pid:{}'.format(pid))
        except Exception as e:
            return {serid: 4}
        else:
            return {serid: 2}


    def restart(self, pids, serid):
        try:
            self.stop(pids, serid)
            self.start(serid)
        except Exception as e:
            return {serid: 4}
        else:
            return {serid: 3}
