import requests
import os

class Download():
	
	__imagetype = ['jpg','png','bmp']
		
	
	def downloadimage(self,url):
		try:
			imagename = url.split('/')[-1]
			res = requests.get(url)
			res.raise_for_status()
			res.encoding = "utf-8"
			#print({'contents':res.content,'imagename':imagename})
			return {'contents':res.content,'imagename':imagename}
		except:
			print("download error")
	
	def requesturl(self,url):
		try:
			headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
			res = requests.get(url,headers=headers)
			res.raise_for_status()
			#res.encoding = "gbk"
			return res.content
		except:
			print("download error")
			
	def download(self,url):
		try:
			imagename = url.split('/')[-1]
			headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
			res = requests.get(url,headers=headers)			
			res.raise_for_status()
			res.encoding = res.apparent_encoding
			#print({'contents':res.content,'imagename':imagename})
			return {'contents':res.text,'imagename':imagename,'binary':res.content}
		except:
			print("download error")
	
		
