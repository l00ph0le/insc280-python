#!/usr/bin/python
import smtplib, string 


HOST = "localhost"
SUBJECT = "Test Email from Nick"
TO = "nmarcoccio@smccme.edu"
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
