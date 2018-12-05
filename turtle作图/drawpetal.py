import turtle
turtle.speed(1)
turtle.setup(500,500,0,0)
for i in range(4):
    turtle.seth(90*(i+1))
    turtle.circle(200,90)
    turtle.seth(-90+i*90)
    turtle.circle(200,90)
