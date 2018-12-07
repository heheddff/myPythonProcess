# coding=gbk
import os

class Save():
	path="./download/"
	count = 0
	
	def __init__(self):
		self.mkdir(self.path)
	
	def save(self,contents,name):
		if contents and name:
			try:
				with open(self.remove_special_characters(name),'wb') as f:
					f.write(contents)
			except Exception as e:
				print(e)
				pass
			else:
				self.count+=1
	#创建文件存放目录
	def mkdir(self,path):
		if os.path.exists(path):
			return
		os.makedirs(path)
	
	#防止重复下载	
	def checkfile(self,name):
		if name == 'temp':
			return
		return os.path.exists(self.remove_special_characters(name))
	
	#确保windows下文件可创建成功
	def remove_special_characters(self,string):
		#windows文件名中不能有下列符号：'\\', '/', ':', '*', '?', '"', '<', '>', '|'
		special_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
		for special_character in special_characters:
			string = string.replace(special_character,'')
		return '/'.join([self.path.strip('/'),string.strip()])+".mp3"
		
		
		
		
