#! /usr/bin/python
# -*- coding:UTF-8 -*-
import codecs
import smtplib
import sys
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import MySQLdb
import unicodecsv as csv
import time 
host = '{mySqlHost}'
username = '{userName}'
password = '{pwd}'
dbname = '{dbName}'
port = {port}
db = MySQLdb.connect(host=host, user=username, passwd=password, db=dbname, charset="utf8", port=port)
cursor = db.cursor()
sql = """
SELECT 
	live_sid AS '公会频道号',
	rank AS '公会排名',
	total_honor AS '公会荣誉',
	now() as '统计时间'
FROM sd_gh_rank ORDER BY total_honor DESC LIMIT 50 
"""
print sql 
localtime = time.asctime(time.localtime(time.time()))
sendDate = time.strftime("%Y-%m-%d",time.localtime())
fileNameOfAnnualRank='/home/jonnyLiu/csv/' + str( sendDate ) + '公会排行榜前50统计.csv'
with open(fileNameOfAnnualRank, 'w') as f:
    f = codecs.open(f.name, "w", "utf-8")
    f.write(u'\ufeff')
    f.close()
cursor.execute(sql)
with open(fileNameOfAnnualRank, 'a') as f:
    fieldNames = ['公会频道号', '公会排名', '公会荣誉', '统计时间']
    w = csv.DictWriter(csvfile=f, fieldnames=fieldNames, encoding='utf-8')
    w.writeheader();
    for row in cursor.fetchall():
        w.writerow({'公会频道号': '\t' + str(row[0]),
                    '公会排名': row[1],
                    '公会荣誉': row[2],
                    '统计时间': row[3]})
me = '{sendEmail}'#发件人邮件
COMMASPACE = ', '
ccs = []
tos = ['{receiverEmail1}','{receiverEmail2}']#收件人列表 用逗号隔开
msg = MIMEMultipart()
msg['Subject'] = (str(sendDate) + '公会排行榜前50统计').decode("utf-8").encode("gbk")
msg['From'] = me
msg['To'] = COMMASPACE.join(tos)
msg['Cc'] = COMMASPACE.join(ccs)

fname = f.name[19:].decode('utf-8').encode('gbk')
print 'fname:',fname

with open(f.name,'rb') as f:
    attach = MIMEApplication(f.read())
    attach.add_header('Content-Disposition','attachment',filename=fname) #添加邮件附件
    msg.attach(attach)
	
s = smtplib.SMTP('smtp.sina.com')#这里以新浪为例
s.login("{sendEmail}", "{sendEmailPwd}")
s.sendmail(me, tos, msg.as_string())
s.quit()
