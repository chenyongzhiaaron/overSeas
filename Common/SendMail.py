#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/10/9 16:32
# @Author  :kira 
# @FileName: SendMail.py

# @Software: PyCharm
import yagmail


def send_mail(report):
    """
    :param report: 需要发送的附件
    :return:
    """
    yag = yagmail.SMTP(user="Kira.chen@starcrownt.com", password="tjmlgtjswwbzqqrc", host="smtp.office365.com")
    subject = "主题，接口自动化测试报告"
    contents = "详情请看附件"
    yag.send(["abc@163.com", "bbb@163.com"], subject, contents, report)
    return print("email has send out!")
