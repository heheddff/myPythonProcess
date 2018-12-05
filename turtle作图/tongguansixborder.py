#绘制嵌套六边形
import turtle
edg = 6
#设置角度
d = 0
#设置边长
k = 10
#设置绘制次数
count = 10
#设置绘制速度
turtle.speed(1)
for i in range(count):
    for j in range(edg):
        turtle.fd(k)
        d+=60
        turtle.seth(d)
        k+=3
