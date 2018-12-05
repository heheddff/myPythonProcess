import time
import re
import json
import bs4
import requests
import pandas

class Spider_Sina():
	
	def __init__(self):
		pass
		#self.download = Download()
		#self.html_parser = Html_Parser()
		#self.url_manager = Url_Manager()
		#self.save_result = Save_Result()
		
	def craw(self):
		pass
		
	def main(self,url):
		pass
		
	def getDetail(self,url):
		res = requests.get(url)
		res.raise_for_status()
		res.encoding = res.apparent_encoding
		result = {}
		soup = bs4.BeautifulSoup(res.text,'html.parser')
		if len(soup.select('.main-title')) > 0 and len(soup.select('.date-source span'))>0:
			result['title'] = soup.select('.main-title')[0].text
			result['dt'] = soup.select('.date-source span')[0].text
			result['newsource'] = soup.select('.date-source a')[0].text
			result['content'] = '\r\n'.join(p.text.strip() for p in soup.select('#article p')[:-1])
			result['editor'] = soup.select('.show_author')[0].text
			result['comments'] = self.getCount(url)
		return result
		
	def getCount(self,url):
		urlTemplate='https://comment.sina.com.cn/page/info?version=1\
&format=json&channel=gn&newsid=comos-{}&group=undefined\
&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&\
thread=1'
		#m = re.search('doc-i(.*).shtml',newsUrl)
		m = re.search('doc-i(.*).shtml',url)
		newid = m.group(1)
		newsurl = urlTemplate.format(newid)
		res = requests.get(newsurl)
		res.encoding="utf-8"
		#print(url)
		return json.loads(res.text.strip('jsonp_1539160569235()'))['result']['count']['total']
		#return json.loads(res.text.strip('jsonp_1539160569235()'))['result']['count']['total']
		
	def parseListLinks(self,url):
		newsdetails = []
		res = requests.get(url)
		res.encoding="utf-8"
		soup = bs4.BeautifulSoup(res.text,'html.parser')
		jd = res.text[26:-14]
		
		js = json.loads(jd)
		#print(js['result']['data'])
		urls = []
		for c in js['result']['data']:
			if self.getDetail(c['url']):
				
				newsdetails.append(self.getDetail(c['url']))
		
		return newsdetails
		
	def parser(self,htmlcontent):
		result = {}
		soup = bs4.BeautifulSoup(htmlcontent,'html.parser')
		if len(soup.select('.main-title')) > 0 and len(soup.select('.date-source span'))>0:
			result['title'] = soup.select('.main-title')[0].text
			result['dt'] = soup.select('.date-source span')[0].text
			result['newsource'] = soup.select('.date-source a')[0].text
			result['content'] = '\r\n'.join(p.text.strip() for p in soup.select('#article p')[:-1])
			result['editor'] = soup.select('.show_author')[0].text
			result['comments'] = self.getCount(url)
			
url='https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback'
news_total=[]

spi = Spider_Sina()

for i in range(1,2):
	newsurl = url.format(i)
	newsary = spi.parseListLinks(newsurl)
	if(len(newsary)>0):
		news_total.extend(newsary)

df = pandas.DataFrame(news_total)
print(df.head())
