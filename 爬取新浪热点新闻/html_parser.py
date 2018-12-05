import bs4
import json
import re
class Html_Parser():
	
	def getCount(self,url):
		urlTemplate = "https://comment.sina.com.cn/page/info?\
		version=1&fo&format=json&channel=gn&newsid=comos-{}\
		&group=undefined&compress=0&ie=utf-8&oe=utf-8&\
		page=1&page_size=3&t_size=3&h_size=3&thread=1"
		
		m = re.search('doc-i(.*).html',url)
		newid = m.group(1)
		newurl = urlTemplate.format(newid)
		res = requests.get(newsurl)
		res.encoding="utf-8"
		return json.loads(res.text.strip('jsonp_1539160569235'))['result']['count']['total']
		
	def parser(self,htmlcontents):
		result = {}
		soup = bs4.BeautifulSoup(res.text,'html.parser')
		if len(soup.select('.main-title')) > 0 and len(soup.select('.date-source span'))>0:
			result['title'] = soup.select('.main-title')[0].text
			result['dt'] = soup.select('.date-source span')[0].text
			result['newsource'] = soup.select('.date-source a')[0].text
			result['content'] = '\r\n'.join(p.text.strip() for p in soup.select('#article p')[:-1])
			result['editor'] = soup.select('.show_author')[0].text
			result['comments'] = self.getCount(url)
		else:
			soup = bs4.BeautifulSoup(res.text,'html.parser')
			jd = res.text[26:-14]
		
			js = json.loads(jd)
			#print(js['result']['data'])
			urls = []
			for c in js['result']['data']:
				if self.getDetail(c['url']):
				
				newsdetails.append(self.getDetail(c['url']))
		
		return newsdetails

	
