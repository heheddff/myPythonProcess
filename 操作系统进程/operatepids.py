# coding=gbk
import psutil
import os
from shutil import copytree
import time
import re
#shutil.copytree(src, dst, symlinks=False, ignore=None, 
#copy_function=copy2, ignore_dangling_symlinks=False)

class Operate_Pids():
	#运营服务器,php生成
	filename = "runservers.ini"
	
	#结束进程
	command = 'taskkill /F  /PID {}'
	
	#基本文件路径
	basepath = "D:\\example\\test\\base_ver"
	
	#目标目录
	dstpath = "D:\\example\\test\\{}"
	
	#cfg配置文件
	cfgfile = "D:\\example\\test\\{}\\cfg\\example.ini"
	
	#启动程序路径
	exe_path = "D:\\example\\test\\{}\\notepad.exe"
	
	#给定默认程序名	
	def __init__(self,pidname='notepad.exe'):
		self.pidname = pidname
	
	#筛选出指定进程	
	def getPid(self):
		pids = psutil.pids()
		pidspath={}
		for pid in pids:
			try:
				p = psutil.Process(pid)
				serverid = 	self.getPidId(p.exe())
				if self.pidname == p.name() and serverid:
					#print(p.exe(),p.name())
					pidspath[pid]=serverid
			except Exception as e:
				#print(e)
				pass
		return pidspath
	
	
	#获取进程所在目录的编号
	def getPidId(self,pidpath):
		#print(pidpath)
		return pidpath.split('\\')[-2] if os.path.exists(pidpath) else False
	
	#配置目录模板
	def pidTemplate(self,serverid):
		return self.dstpath.format(serverid)
		
	#结束进程ID
	def killPid(self,pids):
		if len(pids) > 0:
			for pid in pids:
				#print('成功结束进程:{}'.format(pid))
				os.system(self.command.format(pid))
	
	
	#格式化serverid
	def getServerId(self):
		data = self.getDataFromFile()
		
		if data:
			return set(filter(lambda x:x.strip(),data.split("\n")))
		else:
			return set()
		
		
	#获取文件中运营服务器id
	def getDataFromFile(self):
		if os.path.exists(self.filename):
			try:
				with open(self.filename,'r') as f:
					return f.read().strip('\n')
			except Exception as e:
				print(e)
				return False
		else:
			return False
	
	
	def cpBaseFile(self,dst):
		try:
			copytree(self.basepath,dst)
		except Exception as e:
			print(e)
			pass
	
	
	def mkdirs(self,dirpath):
		dt = time.strftime(" %Y-%m-%d %H-%M-%S",time.localtime())
		if os.path.exists(dirpath):
			try:
				os.rename(dirpath,dirpath+dt)
			except Exception as e:
				print(e)
				pass
		#os.makedirs(dirpath)
	
	
	def createDir(self,servers):
		for serid in servers:
			path = self.pidTemplate(serid)#获取目标目录
			print(path)
			
			self.mkdirs(path)#重命名目录
			self.cpBaseFile(path)#拷贝文件
			self.changeGameIni(serid)#更改配置文件
			self.run(serid)#启动进程
	
	
	def run(self,serid):
		exe_path = self.exe_path.format(serid)
		os.startfile(exe_path)
		
		
	#根据server id更改配置文件内容		
	def changeGameIni(self,serid):
		path = self.cfgfile.format(serid)
		self.writeIni(self.defineRe(self.readIni(path),serid),path)
	
	
	#保存替换后的内容
	def writeIni(self,content,path):
		try:
			with open(path,'w') as f:
				f.write(content)
				f.close()
		except Exception as e:
			print(e)

	
	#替换文件制定内容
	def defineRe(self,txt,serid):
		try:
			txt = re.sub(r'port=2\d+','port=2'+str(serid),txt)
			txt = re.sub(r'groupid=\d+','groupid='+str(serid),txt)
		except Exception as e:
			print(e)
		else:
			return txt
	
	#读取配置文件内容	
	def readIni(self,path):
		try:
			with open(path,'r') as f:
				txt = f.read()
				f.close()
		except Exception as e:
			print(e)
		else:
			return txt
			
			
	def getdiffeId(self,src,dst):
		return src - dst
	
	#获取需要关闭的进程ID
	def getPidBySerId(self,pids,sers):
		waitpids = list()
		for k,v in pids.items():
			for ser in sers:
				if ser == v:
					waitpids.append(k)
		return waitpids
	
	def main(self):
		pids = self.getPid()
		#print(pids)
		#创建新服
		self.createDir(self.getdiffeId(self.getServerId(),set(pids.values())))
		
		#关闭旧服
		waitkillserid = self.getdiffeId(set(pids.values()),self.getServerId())
		#print(waitkillserid)
		waitkillpid = self.getPidBySerId(pids,waitkillserid)
		self.killPid(waitkillpid)
		
	
pids = Operate_Pids()
pids.main()


strs = input("请输入q退出:")
while True:
	if strs.lower() == "q":
		break		
	strs = input("请输入q退出:")
