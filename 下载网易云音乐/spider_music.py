# coding=gbk
from download import Download
from url_manager import Url_Manager
from html_parser import Html_Parser
from save import Save
from set_text_color import Set_Color


class Spider_Music():
	
	def __init__(self):
		self.download = Download()
		self.url_manager = Url_Manager()
		self.html_parser = Html_Parser()
		self.save = Save()
		self.set_color = Set_Color()
		
	def craw(self,url):
		self.url_manager.addurl({'url':url,'name':'temp'})
	
		while self.url_manager.checknewurllength>0:
			newurl = self.url_manager.geturl()
			
			if self.save.checkfile(newurl['name']):
				self.set_color.printDarkRed("{} 已下载！\n".format(newurl['name']))
				continue
			
			print("开始下载 {} {}".format(newurl['name'],newurl['url']))
			htmlcontent = self.download.download(newurl['url'])
			
			if htmlcontent['htmlcontents'] == None:
				self.url_manager.delUrl(newurl)
				self.url_manager.addurl(newurl)			
				
			newurls,result = self.html_parser.parser(htmlcontent)
			
			self.url_manager.addurls(newurls)			
			self.save.save(result,newurl['name'])
			print("下载完成 {} ".format(newurl['name']))
		print("共下载{}首歌曲".format(self.save.count))
		
	def main(self):
		self.craw('https://music.163.com/#/playlist?id=2492536378')

spider = Spider_Music()
spider.main()
