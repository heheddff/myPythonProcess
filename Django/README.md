Version(pip):<br>
celery        3.1.26.post2
Django        2.1.5       
django-celery 3.2.2       
flower        0.9.2
redis         2.10.0
pip           18.1
python        3.6.5

Version(server):
Redis 5.0.3

Example:
vote--模拟Django教程中的投票程序
myblog--模拟blog程序
celeryLearn--模拟Django+django-celery+Flower异步处理

Command
celery worker -A demo -l INFO --启动worker
celery beat -A demo -l INFO --启动定时任务
python3 manage.py runserver 192.168.1.204:7000 --启动Django并指定访问IP和Port
python3 manage.py celery beat -l INFO --启动定时任务(配合Django配置)
python3 manage.py celery worker -l INFO --启动worker（配合Django配置）
python3 manage.py celery flower --basic_auth=admin:607921 --启动flower监控并指定登陆用户名和密码

