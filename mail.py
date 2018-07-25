#!/usr/bin/python
import smtplib, string 


HOST = "localhost"
SUBJECT = "Test Email"
TO = "email@email.edu"
FROM = "fakeemail@spoofed.com"
TEXT = "This is my email message"
BODY = string.join((
	"From: %s" % FROM,
	"To: %s" % TO,
	"Subject: %s" % SUBJECT,
	"",
	TEXT
	), "\r\n")
server = smtplib.SMTP (HOST)
server.sendmail (FROM, [TO], BODY)
server.quit()
