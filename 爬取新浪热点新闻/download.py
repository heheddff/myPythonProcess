import requests
import re

class Download():
	
	def download(self,url):
		m = re.search('doc-i(.*).shtml',url)
		if m:
			return self.getCount(m.group(1))
		else:
			return self.getDetail(url)
	
	def getDetail(self,url):
		try:
			res = requests.get(url)
			res.raise_for_status()
			res.encoding = res.apparent_encoding
		#result = {}
		#soup = bs4.BeautifulSoup(res.text,'html.parser')
		#if len(soup.select('.main-title')) > 0 and len(soup.select('.date-source span'))>0:
		#	result['title'] = soup.select('.main-title')[0].text
		#	result['dt'] = soup.select('.date-source span')[0].text
		#	result['newsource'] = soup.select('.date-source a')[0].text
		#	result['content'] = '\r\n'.join(p.text.strip() for p in soup.select('#article p')[:-1])
		#	result['editor'] = soup.select('.show_author')[0].text
		#	result['comments'] = self.getCount(url)
		#return result
			return {'contents':res.text}
		except Exception as e:
			raise url+' «Î«Û ß∞‹ ' +e
		
	def getCount(self,newid):
		urlTemplate='https://comment.sina.com.cn/page/info?version=1\
			&format=json&channel=gn&newsid=comos-{}&group=undefined\
			&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&\
			thread=1'

		newsurl = urlTemplate.format(newid)
		try:
			res = requests.get(newsurl)
			res.encoding="utf-8"
			res.raise_for_status()
		#print(url)
		#return json.loads(res.text.strip('jsonp_1539160569235()'))['result']['count']['total']
			return {'count':json.loads(res.text}
		except Exception as e:
			raise newsurl + " «Î«Û ß∞‹ "+e
