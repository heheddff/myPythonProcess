# 代码模板    
import turtle  
r = 10
dr = 40
for i in range(4):
    
    turtle.circle(r)
    r+=dr
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(40)
    turtle.seth(0)
    turtle.pendown()
