#date:2018.11.29
#issue:check image before download

from html_parser import HtmlParser
from download import Download
from url_manager import UrlManger
from save_results import SaveResult

class SpiderImages():
	
	#init all instance
	def __init__(self):
		self.download = Download()
		self.htmlparser = HtmlParser()
		self.urlmanager = UrlManger()
		self.saveresult = SaveResult()
	
	def run(self,urls):
		i = 1	
		for url in urls:
			#ile_dir = url.split('/')[-1]
			self.urlmanager.add_new_url(url)

			while self.urlmanager.has_new_url():
				
				new_url = self.urlmanager.get_new_url()
				
				html_cont = self.download.download(new_url)
				
				new_urls,name,html_cont,t = self.htmlparser.parser(html_cont)
				#print(name)
				
				self.urlmanager.add_new_urls(new_urls)
				
				self.saveresult.save(html_cont,name,t)
				print("{} {}".format(i,new_url))
				if i == 100:
					break
				i += 1	
			
			
	def main(self,url):
		#self.craw(url)
		self.run(url)
		
url = [
	"https://trade.1688.com/order/offer_snapshot.htm?buyer_id=674938905&order_entry_id=1179452067840589&is_his=y",
	"https://trade.1688.com/order/offer_snapshot.htm?buyer_id=674938905&order_entry_id=951371180620589&is_his=y",
	]
	
spider = SpiderImages()
spider.main(url)
		
		
