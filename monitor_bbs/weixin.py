from api.src.CorpApi import *


class WeiXin(object):

    def __init__(self, corpid, secrect, agentid, touser, product):
        self.agentid = agentid
        self.touser = touser
        self.product = product
        self.api = CorpApi(corpid, secrect)

    def send(self, msg):
        msg = self.product+":\r\n"+msg
        try:
            response = self.api.httpCall(
                CORP_API_TYPE['MESSAGE_SEND'],
                {
                    "touser": self.touser,
                    "agentid": self.agentid,
                    'msgtype': 'text',
                    #'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                    'text': {
                        'content': msg,
                    },
                    'safe': 0,
                })
            print(response)
        except ApiException as e:
            print(e.errCode, e.errMsg)



