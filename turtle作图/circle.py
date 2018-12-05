import turtle

class DrawCircle():
	
	def __init__(self,n,r):
		self.n = n
		self.r = r
	
	def drawcircle(self):
		turtle.down()#画笔落下
		turtle.circle(self.r)#画半径为r的圆
		turtle.up()#抬起画笔
		turtle.fd(self.r*2)#向前移动一个圆的直径
		
	def movedown(self,i):
		turtle.fd(-i*self.r*2-self.r)#向后移动
		turtle.right(90)#画笔向下旋转90度
		turtle.fd(self.r*2)#画笔向下移动一个圆的距离
		turtle.left(90)#画笔向上旋转90度，回到原点
		turtle.fd(self.r*2)#向前(右)移动一个圆的距离
		
	def run(self):
		for i in range(self.n,1,-1):#步长为1
			for j in range(i):
				self.drawcircle()
			self.movedown(i)
		self.drawcircle()
		
	def main(self):
		self.run()

circle = DrawCircle(5,20)
circle.main()
