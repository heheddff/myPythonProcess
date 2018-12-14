# coding=gbk
import psutil
 
#列出所有进程的PID
pids = psutil.pids()
exe = "pcik_15_dbc_x86_singalsave.exe"

for pid in pids:
	try:
		p = psutil.Process(pid)				
		print(pid,p.exe())
	except Exception as e:
		print(e)
	 
	#获取进行bin的路径
	#try:
	#	print(p.exe())
	#except:
	#	pass
	#获取进程工作目录绝对路径
	#try:
	#	print(p.cwd())
	#except:
	#	pass
	
strs = input("请输入q退出:")
while True:
	if strs.lower() == "q":
		break
		
	strs = input("请输入q退出:")
	 
	#进程的状态
	#print(p.status())
	""" 
	#获取进行bin的路径
	print(p.exe())
			
	#获取进程工作目录绝对路径
	print(p.cwd())
	
	#进程创建的时间
	print(p.create_time())
	 
	#进程uid信息
	print(p.uids())
	 
	#进程gid信息
	print(p.gids())
	 
	#进程CPU时间信息，包括user、system两个CPU时间
	print(p.cpu_times())
	 
	#获取进程cpu的亲和度
	print(p.cpu_affinity())
	 
	#获取进程内存利用率
	print(p.memory_percent())
	 
	#进程内存rss、vms信息
	print(p.memory_info())
	 
	#进程IO信息，包括读写IO数及字节数
	print(p.io_counters())
	 
	#获取打开进程socket的namedutples列表，包括fs、family、laddr等信息
	print(p.connections())
	 
	#进程开启的线程数
	print(p.num_threads())"""

