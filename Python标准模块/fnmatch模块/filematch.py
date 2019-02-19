#Python 3.6.5
#Centos
#参考地址 https://docs.python.org/3/library/fnmatch.html?highlight=fnmatch#module-fnmatch
import fnmatch
import os
pattern = 'access_*.log'#匹配所有
pattern1 = 'access_?.log'#只匹配单个字符
pattern2 = 'access_[23].log'#匹配只包含2或3的文件
pattern3 = 'access_[23]*.log'#匹配以2或3开头的所有文件
pattern4 = 'access_[!2]*.log'#不匹配以2开头的文件
files = os.listdir('.')

for name in sorted(files):
	print("Filename:{:<25} {}".format(name,fnmatch.fnmatch(name,pattern)))#不区分大小写，根据运行环境决定
	print("Casename:{:<25} {}".format(name,fnmatch.fnmatchcase(name,pattern)))#区分大小写
	print("Wenhname:{:<25} {}".format(name,fnmatch.fnmatchcase(name,pattern1)))
	print("Seqname:{:<25} {}".format(name,fnmatch.fnmatchcase(name,pattern2)))
	print("Seqsname:{:<25} {}".format(name,fnmatch.fnmatchcase(name,pattern3)))
	print("NotSeqsname:{:<25} {}".format(name,fnmatch.fnmatchcase(name,pattern4)))
import pprint
pprint.pprint(fnmatch.filter(files,pattern))#filter过滤文件，只显示匹配成功的文件
#print(fnmatch.filter(files,pattern))
pprint.pprint(fnmatch.translate(pattern))

