import socket
import json


class Sockets(object):
    buffer = 1024

    def __init__(self, host='127.0.0.1', port=7899):
        self.ip_port = (host, port)

    def sockets(self, msg):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(3)
        client.sendto(msg.encode('utf-8'), self.ip_port)
        try:
            data, server_addr = client.recvfrom(self.buffer)
        except Exception as e:
            print(e)
        else:
            print('receive data', data, server_addr)
            client.close()

    @staticmethod
    def json_msg(msg):
        res = json.dumps(msg)
        return res

    def send(self, msg):
        try:
            msg = self.json_msg(msg)
            self.sockets(msg)
        except Exception as e:
            print(e)
