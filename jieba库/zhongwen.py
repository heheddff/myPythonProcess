strs = "工业互联网”实施的方式是通过通信、控制和计算技术的交叉应用，建造一个信息物理系统，促进物理系统和数字系统的融合。"
import jieba
ls = strs.replace('”','').replace('、','').replace('，','').replace("。","")
ln = jieba.lcut(ls)
print("中文词语数是：{}".format(len(ln)))
for i in ln:
    print(i,end="/")

words = {}
for word in ln:
    words[word]=words.get(word,0)+1
m=0
n=''

for w in words:
    if m < words[w]:
        n = w
        m = words[w]
    elif m == words[w]:
        n += ' '+w
    print("{}:{}".format(w,words[w]))

print("出现最多的词({}):{}".format(n,m))
