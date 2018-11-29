class UrlManger():
	
	def __init__(self):
		self.wait_urls = set()
		self.downloaded_urls = set()
		
	def add_new_url(self,url):		
		if url and self.checkaddwaiturl(url)  and self.checkaddurldownload(url):
			self.wait_urls.add(url)
		else:
			return
		
	def add_new_urls(self,urls):
		if urls:
			for url in urls:
				self.add_new_url(url)
		
	def has_new_url(self):
		return len(self.wait_urls) != 0
		
	def get_new_url(self):
			download_url = self.wait_urls.pop()
			self.downloaded_urls.add(download_url)
			return download_url
		
	def checkaddwaiturl(self,url):
		if url not in self.wait_urls:
			return True
		else:
			return False
	
	def checkaddurldownload(self,url):
		if url not in self.downloaded_urls:
			return True
		else:
			return False
