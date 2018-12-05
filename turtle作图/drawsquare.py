import turtle

class Squares():
	
	def __init__(self,loop=10,sidesnum=4,k=1,d=0):
		self.loop = loop
		self.sidesnum = sidesnum
		self.k = k
		self.d = 0
		
	def draw(self):
		for i in range(self.loop):
			for j in range(self.sidesnum):
				self.drawsquare()
		turtle.done()#作画完毕窗口不退出
			
	def drawsquare(self):
		turtle.fd(self.k)#向前(右)移动k
		self.d+=91
		turtle.seth(self.d)#旋转海龟角度
		self.k+=2
	
	def main(self):
		self.draw()
		
squares = Squares()		
squares.main()
