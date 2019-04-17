#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import re
from config import configs
from sockets import Sockets
from sendmail import Mail


class MonitorBBS(object):

    def __init__(self):
        # start get configs
        self.base_file = configs['base_file']
        self.bbs_path = configs['bbs_path']
        self.logs_path = configs['logs_path']
        self.bbs_logs = self.bbs_path + self.logs_path
        self.bak_dir = configs['bak_dir']
        self.ip_deny_file = configs['ip_deny_file']
        self.web_server = configs['web_server']
        self.per = configs['per']
        # end get configs
        self.mkdir(self.bbs_path)
        self.init_base_file(self.base_file)
        self.mkdir(self.bak_dir)
        self.bases = self.lists(self.base_file)
        self.block_ip = self.get_block_ip()  # ip黑名单
        self.sockets = Sockets()
        self.mail = Mail(
            configs['mail']['host'],
            configs['mail']['port'],
            configs['mail']['user'],
            configs['mail']['pass'],
            configs['mail']['sender'],
            configs['mail']['receivers'],
            configs['mail']['product'],
        )
        # 输出基础配置
        print(self.base_file)
        print(self.bbs_logs)
        print(self.bak_dir)
        print(self.bbs_path)
        print(self.ip_deny_file)
        print(self.web_server)

    # 初始化模板文件
    def init_base_file(self, path):
        if os.path.exists(path) is False:
            dirs = os.listdir(self.bbs_path)
            f = open(path, "a+")
            for d in dirs:
                print(d)
                f.write(d + "\r\n")
            f.close()

    # 检测目录文件
    @staticmethod
    def lists(path=None):
        lists = set()
        if path is None:
            return lists

        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    lists.add(line.strip("\r\n"))
            return lists

        if os.path.exists(path):
            dirs = os.listdir(path)
            for line in dirs:
                lists.add(line)
        return lists

    # 取差集
    @staticmethod
    def difference_set(src, des):
        return src - des

    # 创建目录
    @staticmethod
    def mkdir(path):
        if os.path.exists(path) is False:
            os.makedirs(path)

    # 剪切文件或目录
    def move_file(self, filename):
        try:
            time_now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
            src = os.path.join(self.bbs_path, filename)
            des = os.path.join(self.bak_dir, filename + "_" + time_now)
            os.rename(src, des)
        except Exception as e:
            print(e)

    # 获取访问日志内容
    def get_log_contents(self):
        day = time.strftime('%d', time.localtime(time.time()))
        # day = 12
        year = time.strftime('%y%m', time.localtime(time.time()))
        login_log = self.bbs_logs.format(year, day)
        if os.path.exists(login_log) is True:
            with open(login_log) as f:
                contents = f.read()
            return contents
        else:
            return False

    # 获取访问ip
    def get_ip_from_log(self, file):
        contents = self.get_log_contents()
        if contents is False:
            return set()
        res = self.patterns(file, contents)
        if len(res) == 0:
            return set()
        else:
            res = ','.join(res)
            ips = self.patterns(file, res, status=2)
            return ips

    # 匹配规则
    @staticmethod
    def patterns(file, contents, status=1):
        pattern = "(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)"
        ip_pattern = re.compile(pattern)
        file_pattern = re.compile(pattern + ".*" + file)
        if file is False:
            return False
        if status == 1:
            res = file_pattern.findall(contents)
        else:
            res = ip_pattern.findall(contents)
        return res

    # 获取ip黑名单
    def get_block_ip(self):
        ip_deny_lists = set()
        if os.path.isfile(self.ip_deny_file):
            with open(self.ip_deny_file) as f:
                for line in f:
                    ip = line.split(" ")[1].strip("\r\n;")
                    ip_deny_lists.add(ip)
                f.close()

        return ip_deny_lists

    # 添加ip到黑名单
    def add_block_ip(self, ip_lists=None):
        if len(ip_lists) == 0:
            return
        count = 0
        template = "deny {0};\n"
        try:
            f = open(self.ip_deny_file, "a+")
            for ip in ip_lists:
                # print(ip)
                if ip not in self.block_ip:
                    count += 1
                    f.write(template.format(ip))
                    self.block_ip.add(ip)  # 添加内存,防止ip过多，可配合NoSQL使用
                    # print(self.block_ip)
            f.close()
        except Exception as e:
            # print('ip_deny_file', self.ip_deny_file)
            print(e)
        finally:
            return count

    # 重启web服务
    def restart_server(self, count=0):
        try:
            if count > 0:
                res = os.system(self.web_server)
                msg = 'server restart success' if res == 0 else 'server restart success fail:' + res
                print(msg)
        except Exception as e:
            print(e)
        

    def send(self, files=None):
        if len(files) == 0:
            return
        self.mail.send("\r\n".join(files))
        for filename in files:
            if filename not in self.bases:
                self.sockets.send(filename)
                self.move_file(filename)
                ip_lists = self.get_ip_from_log(filename)
                count = self.add_block_ip(ip_lists)
                self.restart_server(count)
                # restart web

    def core(self):
        new = self.lists(self.bbs_path)
        files = self.difference_set(new, self.bases)  # 新增文件
        # print(files)
        self.send(files)

    def main(self):
        while True:
            self.core()
            time.sleep(self.per)  # 休眠时间,秒


monitor = MonitorBBS()
monitor.main()

