from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Books(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)#不为空，长度50
    author = Column(String(30),default='未名') #指定默认值
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15),nullable=False,unique=True) #不重复
    summary = Column(String(1000))
    image = Column(String(50))

