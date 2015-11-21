import urllib
import re
from BeautifulSoup import *

position = 18 - 1
count = 7
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Toni.html'

for i in range(count):
	urlHandle = urllib.urlopen(url)
	html = urlHandle.read()
	urlHandle.close()
	
	soup = BeautifulSoup(html)
	linkToFollow = soup('a')[position].get('href',None)
	if linkToFollow != None:
		url = linkToFollow

name = re.findall('known_by_(\S+).html',url)[0]

print name
