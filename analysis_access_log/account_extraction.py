import re
from tools import SavePandas

class AccountExtraction(object):
    contents = []
    accounts = {}
    gameids = {}

    pattern = "register/check/account/.*/gameid/\\d{3}"

    def __init__(self,file):
        self.file = file

    def get_account(self,file):
        i = 0
        try:
            with open(file, "r") as f:
                for line in f.read().split("\n"):
                    i += 1
                    res = self.match(line)
                    if res:
                        data = res.group(0).split("/")
                        self.contents.append({data[2]: data[3], data[4]: data[5]})
                    else:
                        print(res, line)
        except Exception as e:
            print(e)
        else:
            print(i)

    def match(self, content):
        return re.search(self.pattern, content)

    def statistics(self, contents):
        for content in contents:
            account, gameid = content['account'], content['gameid']
            self.accounts[account] = self.accounts.get(account, 0) + 1
            self.gameids[gameid] = self.gameids.get(gameid, 0) + 1

    def main(self):
        print('account start.....')

        if SavePandas.check_file(self.file):
            self.get_account(self.file)
            self.statistics(self.contents)
            print("account all ",len(self.accounts))
            new_accounts = list(self.accounts.items())
            ps = SavePandas('account', new_accounts)
            ps.save_to_excel()
            ps.save_to_sqlite()
        print("end...")
