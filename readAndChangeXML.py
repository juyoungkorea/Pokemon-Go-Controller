import xml.etree.cElementTree as ET
from urllib.request import urlopen
import codecs
import json

lastLat = ""
lastLng = ""

def getPokemonLocation():
	try:
		response = urlopen("http://Project-L2L-iPhone6.local/", timeout = 1)
		reader = codecs.getreader('utf-8')
		return json.load(reader(response))
	except:
		pass
	

def generateXML():
	global lastLat, lastLng
	geo = getPokemonLocation()
	if geo != None:
		if geo["lat"] != lastLat or geo["lng"] != lastLng:
			lastLat = geo["lat"]
			lastLng = geo["lng"]
			gpx = ET.Element("gpx", version="1.1", creator="Xcode")
			wpt = ET.SubElement(gpx, "wpt", lat=geo["lat"], lon=geo["lng"])
			ET.SubElement(wpt, "name").text = "PokemonLocation"
			ET.ElementTree(gpx).write("pokemonLocation.gpx")
			print ("Location Updated!", "latitude:", geo["lat"], "longitude:" ,geo["lng"])

def start():
	while True:
		generateXML()

start()