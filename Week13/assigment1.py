import urllib
import xml.etree.ElementTree as ET

url = raw_input('Please enter the url? ')
data = None
try:
	data = urllib.urlopen(url).read()
except:
	print 'Please enter a correct url'
	quit()
	
tree = ET.fromstring(data)
commentCounts = tree.findall('comments/comment/count')
sumOfCommentCounts = 0
for count in commentCounts:
	sumOfCommentCounts += int(count.text)
	
print sumOfCommentCounts
	


