import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail(object):
    def __init__(self, host, port, user, password, sender, receivers, product):
        self.mail_host = host
        self.port = port
        self.mail_user = user
        self.mail_pass = password
        self.sender = sender
        self.receivers = receivers
        self.product = product
        self.subject = '{0} bbs monitor'.format(self.product)

    def send(self, msg):
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header(self.subject, 'utf-8')
        message['To'] = Header("admin", 'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')

        try:
            mail = smtplib.SMTP(self.mail_host, self.port, timeout=3)
            mail.login(self.mail_user, self.mail_pass)
            mail.sendmail(self.sender, self.receivers, message.as_string())
            print("mail send success")
        except smtplib.SMTPException as e:
            print("Error: mail send failed")
            print(e)

