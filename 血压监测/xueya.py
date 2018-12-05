
#在…处填写多行代码
#在_____出填写一行代码
#可以修改其他代码

fi = open("./files/xueyajilu.txt", 'r',encoding="utf-8")

zb_h = []
zb_l = []
yb_h = []
yb_l = []
zyc = []
yyc = []
xl = []
i=0
for l in fi:
    lls = l.replace('\n','').strip().split(",")
    zb_h.append(eval(lls[1]))
    zb_l.append(eval(lls[2]))
    yb_h.append(eval(lls[3]))
    yb_l.append(eval(lls[4]))
    zyc.append(eval(lls[1]) - eval(lls[2]))
    yyc.append(eval(lls[3]) - eval(lls[4]))
    xl.append(eval(lls[5]))
    i+=1 

fi.close()
cnt = len(xl)
res = []
res.append(list(("高压最大值", max(zb_h),max(yb_h))))
res.append(list(("低压最大值", max(zb_l),max(yb_l))))
res.append(list(("压差平均值", sum(zyc)//cnt,sum(yyc)//cnt)))
res.append(list(("高压平均值", sum(zb_h)//cnt,sum(yb_h)//cnt)))
res.append(list(("低压平均值", sum(zb_l)//cnt,sum(yb_l)//cnt)))
res.append(list(("心率平均值", sum(xl)//cnt)))

zbg = 0
ybg = 0

print('{:<10}{:<10}{:<10}'.format("对比项", "左臂", "右臂"))

for r in range(len(res) - 1):
    print('{:<10}{:<10}{:<10}'.format(res[r][0],res[r][1],res[r][2]))
    if res[r][1] > res[r][2]:
        zbg+=1
    elif res[r][1] == res[r][2]:
        continue
    else:
        ybg+=1

        

if zbg > ybg:
    print('左臂血压偏高',end="")
elif zbg == ybg:
    print('左臂血压与右臂血压相当',end="")
else:
    print('右臂血压偏高',end="")
print(', 心率的平均值为{}'.format(res[5][1]))
