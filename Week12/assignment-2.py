import urllib
from BeautifulSoup import *

urlHandle = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_189578.html')
html = urlHandle.read()
urlHandle.close()

soup = BeautifulSoup(html)

sumOfComments = 0

spans = soup('span')
for span in spans:
	sumOfComments += int( span.contents[0])

print sumOfComments