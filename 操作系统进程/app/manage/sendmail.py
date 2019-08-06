# coding=gbk
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail():
    # ������ SMTP ����
    def __init__(self):
        self.mail_host = "172.20.38.27"  # ���÷�����
        self.mail_user = "mail"  # �û���
        self.mail_pass = "12345"  # ����

        self.sender = 'admin@example.com'
        self.receivers = ['text@example.com']  # �����ʼ���������Ϊ���QQ���������������

    def send(self, msg):
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header("DbView", 'utf-8')
        message['To'] = Header("���̼����", 'utf-8')

        subject = 'DBview������¼'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 Ϊ SMTP �˿ں�
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print("�ʼ����ͳɹ�")
        except smtplib.SMTPException as e:
            print("Error: �޷������ʼ�")
            print(e)
            f = open('error.txt', 'a+')
            f.write(e)
            
if __name__ == '__main__':
	m = Mail()
	m.send('123')
