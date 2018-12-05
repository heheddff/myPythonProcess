import os
import zipfile
import time
import configparser
import re

def checkIp(patten,ip):
    if re.search(patten,ip):
        return True
    else:
        return False

def checkFileType(filename,types):
    t = filename.split('.')[-1]
    if t in types:
        return True
    else:
        return False

def get_filelist(dirnames,filetypes):
    #获取备份文件列表
    filelist = []
    for dirname in dirnames:
        filelist.append(dirname)
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else :
            for root, dirs, files in os.walk(dirname):
                for dirn in dirs:
                    filelist.append(os.path.join(root,dirn))
                for name in files:
                    filename = os.path.join(root, name)
                    if checkFileType(filename,filetypes):
                        filelist.append(filename)
    return filelist
                
def zip_dir(filelist,dirname,zipfilename,srcdirs,delActon):
    #print(zipfilename="D:/bakLog/114/MLOG-114-201810-201810.rar")
    #压缩文件
    
    zipname = zipfilename.split('/')[-1]
    s = time.perf_counter()
    tplt = "{0:-^60}"
    print(tplt.format("文件:"+zipname+"开始压缩"))
    writeLog("文件:"+zipname+"开始压缩")
    
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        print(tar)
        writeLog(tar)
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    else:
        e = time.perf_counter()
        print(tplt.format("文件:"+zipname+"压缩完成"+",耗时:{0:.2f}秒".format(e-s)))
        writeLog("文件:"+zipname+"压缩完成"+",耗时:{0:.2f}秒".format(e-s))
        
    zf.close()

def getMonths(n=3):
    #获取指定日期目录，默认备份前三个月
    year = int(time.strftime('%Y',time.localtime(time.time())))
    month = int(time.strftime('%m',time.localtime(time.time())))
    
    months=[]
    for i in range(1,n+1):
        month-=1
        if month==0:
            month=12
            year-=1
        if month < 10:
            dirname = str(year)+'0'+str(month)
        else:
            dirname = str(year)+str(month)
        #if os.path.exists(dirname):
        #    months.append(dirname)
        #else:
        #    print(dirname,"目录不存在")
        months.append(dirname)
    return months

def checkDir(dirname):
    if os.path.exists(dirname) and os.path.isdir(dirname):
        return True;
    else:
        return False
def checkFile(desfile):
    if os.path.exists(desfile):
        return False;
    else:
        return True
    
def getDir(path,logDir,bakDir,patten):
    #获取ip目录
    res = []
    desDir = []
    srcDir = []
    desFiles = []
    if checkDir(path):
        dirs = os.listdir(path)
        for ip in dirs:
            if checkIp(patten,ip):
                if checkDir(path+ip):
                    ips = ip.split('.')
                    if len(ips) == 4:
                        desDir=bakDir+ips[-1]
                        for log in logDir:
                            if checkDir(path+ip+'/'+log):
                                srcDir=path+ip+'/'+log+'/'
                                desFile=bakDir+ips[-1]+'/'+log+'-'+ips[-1]+'-'
                                res.append([desDir,srcDir,desFile])
            else:
                continue
        return res
    else:
        print('目标文件不存在或非目录')
        writeLog('目标文件不存在或非目录')

def createDesDir(paths):
    
    #创建备份目录
    try:
        os.makedirs(paths)
    except:
        pass
    
def createDesRarFile(filename,srcDirname,months):
    src = []
    se = []
    for month in months:
        if checkDir(srcDirname+month):
            src.append(srcDirname+month)
            se.append(month)

    if len(src) > 0 :
        desfile = filename+se[-1]+'-'+se[0]+'.rar'
        if checkFile(desfile):
            return [src,desfile]
        else:
            return False
    else:
        return False

def readIni():
    cf = configparser.ConfigParser()
    configFile = "zipConfig.conf"
    if os.path.exists(configFile):
        cf.read(configFile)
    
        logType = cf.get("global", "logType").split(',')
        srcDir = cf.get("global", "srcDir")
        bakDir = cf.get("global", "bakDir")
        number = cf.getint("global", "number")
        suffix = cf.get("global", "suffix").split(',')
        iplimit = cf.get("global", "iplimit")
        delAction = cf.getint("global", "delAction")
        #print(srcDir)
    else:
        print("配置文件不存在")
        writeLog("配置文件不存在")
        time.sleep(3)
        exit()
        
    return [logType,srcDir,bakDir,number,suffix,iplimit,delAction]
#转为列表
def ConversionList(ls):
    if type(ls) == type([]):
        return ls
    else:
        return [ls]

def delFile(paths):
    paths = ConversionList(paths)
    for path in paths:
        if checkDir(path):
            if  removeTrees(path):
                try:
                    os.rmdir(path)
                except:
                    print('{0:-^80}'.format(path+'目录删除失败'))
                    writeLog(path+'目录删除失败')
                else:
                    print('{0:-^80}'.format(path+'目录删除成功'))
                    writeLog(path+'目录删除成功')
            else:
                print('{0:-^80}'.format(path+'目录删除失败'))
                writeLog(path+'目录删除失败')
            
            
#递归删除目录文件            
def removeTrees(trees):
    try:
        
        #action = input(">>>确认删除{}目录[y/n]:".format(trees))
        action = 'y'
        if action.lower() == 'y':
            for root, dirs, files in os.walk(trees, topdown=True):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        if len(os.listdir(os.path.join(root, name))) == 0:
                            os.rmdir(os.path.join(root, name))
                        else:
                            removeTrees(os.path.join(root, name))
                            os.rmdir(os.path.join(root, name))
        else:
            return False
    except:
        return False
    else:
        return True
def writeLog(msg):
    file = 'log/' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '.txt'
    fp = open(file,"a")
    msg = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '    '+msg+'\r\n'
    fp.write(msg)
    fp.close()
    pass

def main():
    #需要备份的日志类型
    
    #strs = input("帮助：\nq--退出\nr--运行:\n:")
    strs = 'r'
    if strs.lower() == 'r':
        start = time.perf_counter()
        print("{0:.^80}".format("开始运行"))
        writeLog("开始运行")
        
        #readIni()
        logType,srcPath,bakDirs,number,filesuffix,iplimit,delAction = readIni()
        #print(logType,srcPath,bakDirs,number)
        #源目录
        #srcPath = 'D:/log/'
        #日志备份目录
        #bakDirs = 'D:/bakLog/'
        
        #获取前三个月
        months = getMonths(number)
        #print(months)

        #获取ip目录
        #print(srcPath)
        IpAndDirs = getDir(srcPath,logType,bakDirs,iplimit)
        #print(IpAndDirs)
        
        for i in IpAndDirs:
            createDesDir(i[0])
            
            res = createDesRarFile(i[2],i[1],months)
            if res:
                #print(res)
                srcdirs = res[0]
                #print(srcdirs)
                files = get_filelist(srcdirs,filesuffix)
                zipfilename = res[1]
                desdir = i[1]
                
                zip_dir(files,desdir,zipfilename,srcdirs,delAction)
                if delAction == 1:
                    if not checkFile(zipfilename):
                        delFile(srcdirs)
                    
        end = time.perf_counter()                
        print("{0:.^80}".format("运行结束"))
        writeLog("运行结束")
        
        print("总耗时：{0:.2f}秒".format(end-start))
        writeLog("总耗时：{0:.2f}秒".format(end-start))
        
        time.sleep(3)
        #strs = input("是否退出程序[y/n]:")
        strs='y'
        while strs.lower() != 'y':
            strs = input("是否退出程序[y/n]:")
        
    else:
       main()    

main()

