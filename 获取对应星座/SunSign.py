#SunSign.csv
f = open("./files/SunSign.csv","r",encoding="utf-8")
name = []
item = {}
inp = list()
for line in f:
    ls = line.replace('\n','').split(",")
    name.append(ls[0])
    item[ls[0]]=ls[1:]

while True:
    ch = input("")
    if ch == 'exit':
        break
    inp.append(ch)
#print(inp)
for i in inp:
    if item.get(i,False):
        data = item.get(i)
    #print(data)
    
        print("{2}座的生日位于{0}-{1}之间。".format(data[0],data[1],chr(eval(data[2]))))
    else:
        print("输入星座名称有误！")
