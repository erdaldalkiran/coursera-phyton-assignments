import urllib
import json

placeToFind = raw_input('Place to find?')
if len(placeToFind) < 1: exit(0)

baseUrl = 'http://python-data.dr-chuck.net/geojson'
parameters = '?'+ urllib.urlencode({'sensor':'false', 'address': placeToFind})
urlData = urllib.urlopen(baseUrl + parameters).read()

data= json.loads(urlData)

print data['results'][0]['place_id']
	