from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

def notify(filename):
	email_sender = "Enter email of sender"
	password = "Create a new app password with the name python in the email settings and paste the password here"
	email_receiver = "Enter email of receiver"
	subject="Person Detected"
	body="Person Detected at {}".format(str(datetime.now()))

	ema = MIMEMultipart()
	ema["From"] = email_sender
	ema["To"] = email_receiver
	ema["subject"] = subject
	text = MIMEText("SUCCESS")
	ema.attach(text)
	with open(filename+".jpg", 'rb') as f:
		img_data = f.read()

	image = MIMEImage(img_data, name=os.path.basename(filename))
	ema.attach(image)
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
		smtp.login(email_sender,password)
		smtp.sendmail(email_sender,email_receiver,ema.as_string())