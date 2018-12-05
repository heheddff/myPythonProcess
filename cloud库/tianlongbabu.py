import jieba
f = open("./files/天龙八部-网络版.txt","r",encoding="utf-8")
ln = f.read().replace(" ",'').replace("\n","")
f.close()
ls = list(ln)
counts={}
for i in ls:
    counts[i]=counts.get(i,0)+1
strs=''
for words in counts:
    strs += "{}:{},".format(words,counts[words])
fw = open("files/天龙八部-汉字统计.txt","w",encoding="utf-8")
fw.write(strs)
fw.close

excu = "？，。！：、“”"
ls = jieba.lcut(ln)

wordscount={}
for w in ls:
    if w not in excu and len(w)>1:
        wordscount[w]=wordscount.get(w,0)+1
newitems =list(wordscount.items())
newitems.sort(key=lambda x:x[1],reverse=True)
wc=''
for i in newitems:
    k,v = i
    wc+="{}:{},".format(k,v)
fwc = open("files/天龙八部-词语统计.txt","w",encoding="utf-8")
fwc.write(wc[0:-1])
fwc.close()
    #print("{}:{}".format(k,v))

import wordcloud
s = wordcloud.WordCloud(font_path="files/FZSTK.TTF", \
                        width=800,height=600)
s.generate(" ".join(ls))
s.to_file("tlbb.png")
