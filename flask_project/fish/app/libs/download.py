#urllib,requests
import requests


class DOWNLOAD(object):

    #转为静态方法
    @staticmethod
    def get(url,return_json=True):
            res = requests.get(url)
            return res.json() if return_json else res.text

    def post(self):
        pass