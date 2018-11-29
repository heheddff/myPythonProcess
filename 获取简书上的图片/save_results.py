import os

class SaveResult():
	
	root = './download'
	
	def __init__(self,path='./temp'):
		self.path=path
		#self.root = '/'.join([self.__root,path])
		#self.__createDir()
		
	def saveimage(self,res):
		imagename = '/'.join([self.__root.strip('/'),res['imagename']])
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
		self.__root = '/'.join([self.root,path])
		print(self.__root)
		
		if os.path.exists(self.__root):
			return
		os.makedirs(self.__root)
		
	def __checkfile(self,filename):
		return os.path.exists(filename)
	
	def __checkfiletype(self,filename):
		return filename if filename.rfind('.') >0 else '.'.join([filename,'jpg'])
	
	def save(self,contents,file_dir,author,t):
		if t == 1:
			self.createDir('/'.join([author,file_dir]))
		else:
			self.saveimage(contents)
