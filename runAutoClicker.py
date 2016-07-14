import os
from urllib.request import urlopen
import json
import codecs
import time

def checkConnected():
	try:
		response = urlopen("http://Project-L2L-iPhone6.local/", timeout = 1)
		reader = codecs.getreader('utf-8')
		return json.load(reader(response))
	except:
		pass
	

def clickAction():
	os.system("./autoClicker -x 600 -y 1050")
	os.system("./autoClicker -x 600 -y 1100")
	time.sleep(1)
	print ("clicking!!")

def start():
	while True:
		if checkConnected() != None:
			clickAction()

start()