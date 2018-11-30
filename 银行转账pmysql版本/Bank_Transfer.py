# coding=gbk
import pymysql

class Money():
	def __init__(self,sid,tid,mon):
		self.conn = pymysql.connect(
			host="127.0.0.1",
			port=3306,
			user='root',
			passwd='****',
			db='test'
			)
		self.cursor = self.conn.cursor();
		self.table = "money"
		self.sid = sid
		self.tid = tid
		self.mon = mon
	
	def checkuser(self,userid):
		try:
			sql = "select userid from "+self.table+" where userid=%s"
			self.cursor.execute(sql,(userid,))
			res = self.cursor.fetchone()
			if res is None:
				raise Exception("账号{}不存在".format(userid))
		finally:
			pass
			#self.cursor.close()
			#self.conn.close()
			
	
	def reducemoney(self,userid,money):
		try:
			sql = "update "+self.table+" set money=money-%s where userid=%s"
			self.cursor.execute(sql,(money,userid))
			
			if self.cursor.rowcount != 1:
				raise Exception("账号{}转账失败".format(userid))
		finally:
			pass
			#self.cursor.close()
			#self.conn.close()
	
	def addmoney(self,userid,money):
		try:
			sql = "update "+self.table+" set money=money+%s where userid=%s"
			self.cursor.execute(sql,(money,userid,))
			
			if self.cursor.rowcount != 1:
				raise Exception("账号{}收账失败".format(userid))
		finally:
			pass
			#self.cursor.close()
			#self.conn.close()
		
	def checkmoney(self,userid,money):
		try:
			sql = "select userid from "+self.table+" where userid=%s and money>%s"
			self.cursor.execute(sql,(userid,money))
			res = self.cursor.fetchone()
			if res is None:
				raise Exception("账号{}余额小于{}".format(userid,money))
		finally:
			pass
			#self.cursor.close()
			#self.conn.close()
		
	def run(self):
		try:
			self.checkuser(self.sid)
			self.checkuser(self.tid)
			self.checkmoney(self.sid,self.mon)
			self.reducemoney(self.sid,self.mon)
			self.addmoney(self.tid,self.mon)
			self.conn.commit()
		except Exception as e:
			self.conn.rollback()
			raise e
		finally:
			#pass
			self.cursor.close()
			self.conn.close()
try:		
	m = Money(11,13,100)
	m.run()
except Exception as e:
	#pass
	print(e)
else:
	print("转账成功")

	
