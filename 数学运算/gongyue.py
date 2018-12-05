#求公约数
def getMax(x,y):
    if x < y:
        x,y = y,x
    while (x%y) !=0:
        r = x%y
        x = y
        y = r
    return y
a = eval(input("输入整数"))
b = eval(input("输入整数"))
print(getMax(a,b))
