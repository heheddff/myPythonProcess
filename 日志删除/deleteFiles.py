import os
#This program will delete files except in the __filelists
class DeleteFiles(object):
	__filelists = [
			'notify_requests.log',
			'notify_requests.log',
			'receipts.log',
			'receipts.log'
		]
	
	def __init__(self,root=""):
		self.root = root
		#self.walkDir(self.root)
	
	#check path exists
	def checkPath(self,path):
		return  True if os.path.exists(path) else False
	
	#check is dirs
	def checkDir(self,path):
		return True if os.path.isdir(path) else False
		
	#change list
	def changeList(self,roots):
		
		return roots.split(',')
		
	#walk dir
	def walkDir(self,dirPath):
		lists = []
		if self.checkPath(dirPath) and self.checkDir(dirPath):
			for root,dirs,files in os.walk(dirPath):
				for filename in files:
					if filename not in self.__filelists:
						filepath = root+"/"+filename
						try:
							os.remove(filepath)
						except:
							print(filepath +' delete fail')
						else:
							print(filepath + ' delete success')
		else:
			print(self.root+" is wrong")
	def main(self):
		for root in self.changeList(self.root):
			self.walkDir(root)
		
print('please input dirpath,if you have more dirpathes,Separated by commas(,)')					
path = input(":")

deletefiles = DeleteFiles(root=path)
deletefiles.main()

#print(res)

strs = input('q--quit:')
while strs.lower() != 'q':
	strs = input('q--quit:')
					
			
