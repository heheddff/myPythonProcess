# coding=gbk
import re
import requests
from selenium import webdriver
import random
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


class Download():
	
	__uas = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    ]
	
	__ips = []
	
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
		#self.__ips = self.get_ip()
	
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
	
	#未找到高可用代理，功能暂时停止
	def get_ip(self):
		url = "https://www.kuaidaili.com/free/inha/1/"
		res = requests.get(url)
		soup = BeautifulSoup(res.text,'html.parser')
		data = soup.find(id="list").find('tbody').find_all('tr')
		ip_compile= re.compile(r'<td data-title="IP">(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
		port_compile = re.compile(r'<td data-title="PORT">(\d+)</td>')                # 匹配端口
		ip = re.findall(ip_compile,str(data))       # 获取所有IP
		port = re.findall(port_compile,str(data))   # 获取所有端口
		return [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080
		
        
        		
	def getmusic(self):
		try:
			url = self.getrealurl()
			host = url.strip('http://').split('/')[0]
			headers = {
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
				"Accept-Encoding": "gzip, deflate",
				"Accept-Language": "zh-CN,zh;q=0.9",
				"Host": host,
				"User-Agent": self.__uas[random.randint(0,6)]#模拟不同浏览器
				}
			ip = random.choice(self.__ips)
			proxies = {
				'http':'http://'+ip,
				'https':'http://'+ip
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
			#brower = webdriver.PhantomJS(r'D:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe')#r防止转义，phantomjs可以添加到PATH路径
			#help(webdriver)
			chrome_options = Options()
			chrome_options.add_argument('--headless')
			chrome_options.add_argument('--disable-gpu')			
			brower = webdriver.Chrome("D:\\tools\\chromedriver_win32\\chromedriver.exe",options=chrome_options)#创建driver,参数为插件的路径
			brower.get(self.url)
			brower.switch_to.frame(brower.find_element_by_name("contentFrame"))#切换到指定框架
		except Exception as e:
			print(e)
			return
		else:
			return brower.page_source
		
#d=Download()
#print(d.get_ip())
#res = d.download('http://music.163.com/song/media/outer/url?id=28160459.mp3')
#print(res['identify'])
#print(res['htmlcontents'])
