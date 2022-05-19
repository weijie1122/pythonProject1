import smtplib
import os
import logging
import yagmail
from comm import FilePath
from conf.config import email
def send_email():
    sender=email['sender']
    senderpassword=email['senderpassword']
    receivers=email['receivers']
    host='smtp.qq.com'
    attachments=FilePath.path_file('report','index.html')
    title='自动化测试报告'
    contents = 'sddsdsdsdsds<!DOCTYPE html><html lang="en"> <body > <iframe name="my-iframe" id="my-iframe" src="http://desktop-3827u2j:9999/index.html" frameborder="边框（一般为0）" width="100%" height="900" scrolling="是否滚动（一般为“no”）"></iframe> </body> </html>'
    yag=yagmail.SMTP(sender,senderpassword,host)
    yag.send(to=receivers,subject=title,contents=contents,attachments=attachments)
    return
a=send_email()

