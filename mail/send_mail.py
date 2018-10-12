import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os

def send_mail(address,message):
	from_addr = "bacardibr@163.com"
	to_addr = ["cheng.shen@columbia.edu","bacardibr@163.com"]
	print(type(to_addr))
	msg =MIMEMultipart()
	msg['From'] = from_addr
	msg['To'] = address
	msg['Subject'] = Header(u'今天又是美好的一天', 'utf8').encode()


	body = "完成这些作业\n "
	print(type(body))
	msg.attach(MIMEText(body,'plain','utf-8'))
	img_data = open('corgi.jpg','rb').read()
	image = MIMEImage(img_data,_subtype = "jpg",name = os.path.basename('corgi.jpg'))
	msg.attach(image)

	server = smtplib.SMTP('smtp.163.com',25)
	server.ehlo()
	server.starttls()
	server.login(from_addr,'sc6229617')
	text= msg.as_string()
	server.sendmail(from_addr,to_addr,text)
	server.quit()

while True:
	addr = input()
	mess = input()
	print(type(addr))
	print(type(mess))
	send_mail(addr,mess)