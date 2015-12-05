import json
import urllib

url = raw_input('Url to retrieve comments?')
if len(url) < 1 : exit(0)

urlData = urllib.urlopen(url).read()

data = json.loads(urlData)

sumOfCounts = 0
for comment in data['comments']:
	sumOfCounts += comment['count']

print sumOfCounts