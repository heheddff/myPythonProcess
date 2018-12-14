# coding=gbk
class Url_Manager():
	
	__newurl = list()	#存放未下载的url
	__oldurl = list()	#存放已下载的url
	
	def addurl(self,url):
		if url == None:
			return
		if self.checkurl(url):
			self.__newurl.append(url)
		
	def addurls(self,urls):
		if urls == None:
			return
			
		for url in urls:
			self.addurl(url)
		
	def geturl(self):
		newurl = self.__newurl.pop()
		self.__oldurl.append(newurl)
		return newurl
	
	def delUrl(self,url):
		if url in self.__oldurl:
			self.__oldurl.remove(url)
		
		
	@property	
	def checknewurllength(self):
		return len(self.__newurl)
	
	def checkurl(self,url):
		if url not in self.__newurl and url not in self.__oldurl:
			return True
		else:
			return False


