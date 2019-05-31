import json
import os
import time
import random
import requests
from tools import SavePandas


class IpFilter(object):
    api = "http://ip.taobao.com/service/getIpInfo.php?ip={}"
    ip_log = "ip.log"
    contents = []
    max = 1000

    def __init__(self, file):
        self.file = file

    @staticmethod
    def read_file(file):
        res = {}
        m = 0
        n = 0
        with open(file, "r") as f:
            for line in f.read().split("\n"):
                n += 1
                try:
                    data = json.loads(line)
                    ip = data['ip']
                    res[ip] = res.get(ip, 0) + 1
                except Exception as e:
                    m += 1
                    print(line, e)
        return res if len(res) > 0 else False

    def get_local(self, ip):
        api = self.api.format(ip)
        try:
            res = requests.get(api)
            # res.encoding = "utf-8"
            js = json.loads(res.text)
        except Exception as e:
            print(api, e)
            return False
        else:
            if js['code'] == 0:
                return js['data']
            else:
                print(js)
                return False

    def save_ip(self, ips):
        with open(self.ip_log,"a+") as f:

            for ip in ips:
                f.write(ip[0]+","+str(ip[1])+"\n")

    def select(self, ips):
        wait_ips = {}
        i = 0
        for ip in ips:
            i += 1
            print(i, ip)
            data = self.get_local(ip)
            if data:
                data['count'] = ips[ip]
                self.contents.append(data)
            else:
                wait_ips[ip] = ips[ip]
            wait_time = random.randint(10, 20) / 10
            print('wait_time=', wait_time)
            time.sleep(wait_time)
        if wait_ips:
            print('waitips length=', len(wait_ips.keys()))
            print(wait_ips)
            self.select(wait_ips)
        else:
            print('ip 查询结束')

    def get_top1000(self):
        ips = {}
        with open(self.ip_log, "r") as f:
            for line in f.read().split("\n"):
                try:
                    d = line.split(",")
                    ip, num = d[0], int(d[1])
                    if num > self.max:
                        ips[ip] = num
                except Exception as e:
                    print(e)
        return ips

    def main(self):
        print("start....")
        if SavePandas.check_file(self.file):
            # res = self.read_file(self.file)
            # print(res)
            # new_res = self.sort_by_num(res)
            # del res
            # self.save_ip(new_res)
            # del new_res
            ips = self.get_top1000()
            self.select(ips)
            # print(self.contents)
            ps = SavePandas('ip', ips)
            ps.save_to_excel()
            ps.save_to_sqlite()
        print("end....")





