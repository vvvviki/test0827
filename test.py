# coding:utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import sys,datetime,smtplib
reload(sys)
sys.setdefaultencoding("utf-8")

print "123456la"

now = datetime.datetime.now() #获取当前时间

#邮件发送设置
smtpserver = 'smtp.qq.com'  #邮箱服务器地址
smtpport = 587							#邮箱服务器地址端口
emailuser = '329859252@qq.com'	#发件人邮箱
emailpasswd = 'ocooylycsgnmbjcg'				#发件人邮箱密码
emailreceiver = ['79573245@qq.com'] #收件人邮箱


#设置邮件相关信息
msg = MIMEMultipart()
msg['Subject'] = 'just test  {}'.format(now.strftime("%Y-%m-%d %H:%M:%S"))
msg['From'] = emailuser
msg['To'] = ','.join(emailreceiver)
msg['Accept-Language'] = 'zh-CN'
msg['Accept-Charset'] = 'ISO-8859-1,utf-8'

puretext = MIMEText('哈哈，测试自动化脚本集成','plain','utf-8')
msg.attach(puretext)

#开始真正的发送邮件了
try:
	client = smtplib.SMTP()
	# client.set_debuglevel(1)
	client.connect(smtpserver, smtpport)
	client.ehlo()
	client.starttls()
	client.login(emailuser, emailpasswd)
	client.sendmail(emailuser, emailreceiver, msg.as_string())
	client.quit()
except smtplib.SMTPRecipientsRefused:
	print 'Recipient refused'
except smtplib.SMTPAuthenticationError:
	print 'Auth error'
except smtplib.SMTPSenderRefused:
	print 'Sender refused'
except smtplib.SMTPException, e:
	print e.message