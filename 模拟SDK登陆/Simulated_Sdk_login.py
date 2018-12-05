import hashlib
import requests
import json
import datetime
import time

class Sdk_Login():
	__url = "http://debug.example.com/index.php"
	__userfile = "user.txt"
	
	m = 0
	n = 0
	
	#this function will use to get secretct and sessionid
	def getSecret(self):
		data = {
		"dev_hash": "86dac181ee38043c195c427c5502965a",
		"dev_network_type":"9",
		"from_ad_id":"0",
		"from_site_id":"0",
		"game_id":"3001",
		"package_name":"com.iccgame.sdk",
		"package_signature_hash":"00000000000000000000000000000000",
		"package_version":"2.0",
		"version":"0",
		"module":"GAME.Sessions.Create",
		"runModel": "user"
		}
		try:
			res = requests.post(self.__url,data=data)
			res.encoding=res.apparent_encoding
			res.raise_for_status()
			js = json.loads(res.text)
		except Exception as e:
			raise e
		else:
			self.saveRequest(res.text)
			self.saveRequest(str(res.cookies))
			return [js['data'][0]['args'][0]['sessionSecret'],res.cookies.get_dict()]
			
	#this function is md5 userpassword
	def md5str(self,strs):
		try:
			m = hashlib.md5()
			secret = strs.encode(encoding='utf-8')
			m.update(secret)
			md5req = m.hexdigest()
			self.saveRequest(json.dumps({strs:md5req}))
			return md5req
		except Exception as e:
			raise e
			
			
	#this function will use to get login	
	def login(self,username="",userpass="",cookies=''):
		
		data = {
		"dev_hash": "86dac181ee38043c195c427c5502965a",
		"dev_network_type": 9,
		"from_ad_id": 0,
		"from_site_id": 0,
		"game_id": 3001,
		"package_name": "com.iccgame.sdk",
		"package_signature_hash": "00000000000000000000000000000000",
		"package_version": "2.0",
		"version": "0",
		"module":"GAME.Accounts.Login",
		"acct_name": username,
		"acct_secret":userpass,
		}
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36",
			}
		try:
			res = requests.post(self.__url,data=data,cookies=cookies,headers=headers)
			res.encoding=res.apparent_encoding
			res.raise_for_status()
		except Exception as e:
			self.m+=1
			self.saveRequest(str(e))
			raise e
		else:
			self.n+=1
			self.saveRequest(res.text)
			return res.text
			
	def getUser(self):
		try:
			with open(self.__userfile,'r') as f:
				txt = f.read()
				f.close()
		except Exception as e:
			raise e
		else:
			return txt
	
	def formatData(self,data):
		res = {}
		try:
			data = data.strip("\n").split("\n")
			for line in data:
				users = line.split("\t")
				res[users[0]] = users[1]
		except Exception as e:
			raise e
		else:
			return res		
		
	
	def saveRequest(self,msg):
		try:
			filename = str(datetime.date.today())+".log"
			msgtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
			msg = msgtime+"\t"+msg+"\n"
			with open(filename,'a') as f:
				f.write(msg)
				f.close()
		except Exception as e:
			raise e
		
	def main(self):
		try:
			filedata = self.getUser()
			userdatas = self.formatData(filedata)
			i = 1
			for username,userpass in userdatas.items():
				print("{}	{}".format(i,username))
				self.saveRequest(username+"\t"+userpass)
				usermd5 = self.md5str(userpass)
				strs = self.getSecret()
				userpass = self.md5str(strs[0]+usermd5)
				self.login(username,userpass,strs[1])
				i +=1
				time.sleep(4)		
		except Exception as e:
			raise e
try:
	sdk = Sdk_Login()
	sdk.main()
	print("fail {}".format(sdk.m))
	print("success {}".format(sdk.n))
except Exception as e:
	print(e)
		
