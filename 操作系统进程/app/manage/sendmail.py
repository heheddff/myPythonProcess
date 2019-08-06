# coding=gbk
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail():
    # 第三方 SMTP 服务
    def __init__(self):
        self.mail_host = "172.20.38.27"  # 设置服务器
        self.mail_user = "mail"  # 用户名
        self.mail_pass = "12345"  # 口令

        self.sender = 'admin@example.com'
        self.receivers = ['text@example.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def send(self, msg):
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header("DbView", 'utf-8')
        message['To'] = Header("进程检测结果", 'utf-8')

        subject = 'DBview操作记录'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)
            f = open('error.txt', 'a+')
            f.write(e)
            
if __name__ == '__main__':
	m = Mail()
	m.send('123')
