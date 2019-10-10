#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/9/27 14:19
# @Author  :kira 
# @FileName: configEmail.py

# @Software: PyCharm
import os
import yagmail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMail():
    def send_mail(self):
        subject = 'Python send mail test'
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_new = file + "./Log.txt"
        with open(file_new, 'rb') as f:
            send_att = f.read()
        att = MIMEText(send_att, 'text', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Conten-Disposition'] = 'attachment; filename="Log.txt"'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect('smtp.office365.com', 993)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user='Kira.chen@starcrownt.com', password="tjmlgtjswwbzqqrc")
        smtp.sendmail("Kira.chen@starcrownt.com")
        smtp.quit()
        return print("send success")

    def do_mail(self):
        yag = yagmail.SMTP(user="Kira.chen@starcrownt.com", password="tjmlgtjswwbzqqrc", host="smtp.office365.com")
        contents = "this is the body,test"
        yag.send("Kira.chen@starcrownt.com", "subject", contents)


if __name__ == "__main__":
    action = SendMail()
    # action.do_mail()
    action.send_mail()
