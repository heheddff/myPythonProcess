# coding=gbk
import re
import requests
from selenium import webdriver

class Download():
	
	headers = {
			#"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'Referer':'http://music.163.com/',
			'Host':'music.163.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "zh-CN,zh;q=0.9"
			}
	
	def __init__(self):
		self.url = ''
	
	def download(self,url):
		self.url = url
		#print(url)
		return self.patterns		
	
	@property
	def patterns(self):
		playlist = re.compile("playlist\?id=\d+")	#匹配歌单
		song = re.compile("song/media/outer/url\?id=\d+")	#匹配下载地址
		
		res = {
			'identify':False,
			'htmlcontents':'',
		}
		
		if re.search(song,self.url):
			res['identify'] = 1
			res['htmlcontents'] = self.getmusic()	#用于获取mp3
		elif re.search(playlist,self.url):
			res['identify'] = 2
			res['htmlcontents'] = self.geturl()	#获取网页内容
			
		return res
			
	def getmusic(self):
		try:
			url = self.getrealurl()
			host = url.strip('http://').split('/')[0]
			headers = {
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
				"Accept-Encoding": "gzip, deflate",
				"Accept-Language": "zh-CN,zh;q=0.9",
				"Host": host,
				"User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
				}
			
			res = requests.get(url,headers=headers)
		except Exception as e:
			print(e)
			return
		else:
			return res.content
			
	def getrealurl(self):
		res = requests.get(self.url,headers=self.headers)
		return res.url
			
	def geturl(self):
		try:
			brower = webdriver.PhantomJS(r'D:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe')#r防止转义，phantomjs可以添加到PATH路径
			brower.get(self.url)
			brower.switch_to.frame(brower.find_element_by_name("contentFrame"))#切换到指定框架
		except Exception as e:
			print(e)
			return
		else:
			return brower.page_source
		
#d=Download()
#res = d.download('http://music.163.com/song/media/outer/url?id=28160459.mp3')
#print(res['identify'])
#print(res['htmlcontents'])
