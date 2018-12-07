from bs4 import BeautifulSoup

class Html_Parser():
	baseurl = "http://music.163.com/song/media/outer/url?{}.mp3"
	
	def parser(self,res):
		
		if res.get('identify') == 1:
			#print(res['identify'])
			return None,res.get('htmlcontents',False)
			
		else:
			return self.geturls(res['htmlcontents'])
	
	def geturls(self,htmlcontent):
		#print(htmlcontent)
		newsurl=list()
		try:
			soup = BeautifulSoup(htmlcontent,'html.parser')
			songlist = soup.find('table').find_all('tr')[1:]
		
			for link in songlist:
				url = self.baseurl.format(link.find_all('td')[1].find('a')['href'].split('?')[-1])
				name = link.find_all('td')[1].find('a').find('b')['title']
				newsurl.append({'url':url,'name':name})
		except Exception as e:
			print(e)
			pass
		else:
			return newsurl,False
	
