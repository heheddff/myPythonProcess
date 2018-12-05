import jieba
def readFile(filename):
    f = open(filename,"r")
    ls = f.read()
    ls =ls .replace("\n","")
    f.close()
    return ls
def fence(ls):
    ln = jieba.lcut(ls)
    count={}
    exc=[" ","，","\u3000","\"","。","：","…","！","？","、"]
    for i in ln:
        if i not in exc:
            count[i]=count.get(i,0)+1
    return count
def sortWords(words):
    words = list(words.items())
    words.sort(key=lambda x:x[1],reverse=True)
    newlist = []
    for i in range(100):
        newlist.append(words[i])
    return newlist

def showWords(wordslist):
    data = ""
    for i in range(len(wordslist)):
        key,va = wordslist[i]
        data += "{}:{},".format(key,va)
    return data[0:-1]
def writeWords(filename,content):
    f = open(filename,"w")
    f.write(content)
    f.close()

def main(src,des):
    ls = readFile(src)
    words = fence(ls)
    #print(words)
    wordslist = sortWords(words)
    #print(wordslist)
    content = showWords(wordslist)
    #print(content)
    writeWords(des,content)
    
def compares(s,t):
    st = s&t
    return st

def changeSet(strs):
    ls=strs.split(",")
    s=set()
    for i in ls:
        s.add(i.split(":")[0])
    return s

name = ['命运','寻梦']
#for i in name:
    #main("files/"+i+"-网络版.txt","files/"+i+"-字符统计.txt")
s = readFile("files/命运-字符统计.txt")
t = readFile("files/寻梦-字符统计.txt")
res = compares(changeSet(s),changeSet(t))
for i in res:
    print(i)
print(len(res))
