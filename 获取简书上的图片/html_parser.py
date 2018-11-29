from bs4 import BeautifulSoup

class HtmlParser():
	
	__name = ''
	
	
	def getauthor(self,html_content):
		if not html_content:
			return
		
		try:
			soup = BeautifulSoup(html_content,"html.parser")			
			name = soup.find("div",class_="author").find_all(class_='info')[0].find('a').text
		except:
			return 'temp'
		else:
			return name

	def getimages(self,html_content):
		if not html_content:
			return
			
		soup = BeautifulSoup(html_content,"html.parser")
		images = soup.find("div",class_="show-content-free").find_all('img')
		new_images = []
		for image in images:
			try:
				#print(image)
				new_images.append("http:"+image['data-original-src'])
			except:
				continue
		return new_images

	def parser(self,html_content):
		try:
			soup = BeautifulSoup(html_content['contents'],"html.parser")
			name = soup.find("div",class_="author").find_all(class_='info')[0].find('a').text
			images = soup.find("div",class_="show-content-free").find_all('img')
			new_images = []
			for image in images:
				new_images.append("http:"+image['data-original-src'])
			return new_images,name,html_content,1
		except:
			return '','',html_content,0
			
