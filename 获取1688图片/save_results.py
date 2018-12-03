import os

class SaveResult():
	
	__root = './download'
	
	def __init__(self):
		pass		
		
	def saveimage(self,res):
		imagename = '/'.join([self.root.strip('/'),res['imagename']])
		imagename = self.__checkfiletype(imagename)
		
		if self.__checkfile(imagename):
			print('{} is exists'.format(imagename))
		else:
			try:
				with open(imagename,"wb") as f:
					f.write(res['binary'])
					f.close()
			except:
				print("save image fail")	
	
	def createDir(self,path):
		self.root = '/'.join([self.__root,path])
		
		if os.path.exists(self.root):
			return
		os.makedirs(self.root)
		
	def __checkfile(self,filename):
		return os.path.exists(filename)
	
	def __checkfiletype(self,filename):
		return filename if filename.rfind('.') >0 else '.'.join([filename,'jpg'])
	
	def save(self,contents,author,t):
		if t == 1:
			self.createDir(author)
		else:
			self.saveimage(contents)
