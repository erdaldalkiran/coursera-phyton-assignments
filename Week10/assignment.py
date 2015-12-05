
fileName = raw_input('Please enter the file to open?')
if len(fileName) <1: fileName = 'mbox-short.txt'

fileHandle = None
try:
	fileHandle = open(fileName)
except:
	print 'unable to open file'
	exit(0)

hoursDic = {}
for line in fileHandle :
	if line.startswith('From '):
		time = line.split()[5]
		hour = time.split(':')[0]
		hoursDic[hour] = hoursDic.get(hour, 0) + 1

fileHandle.close()

for key,value in sorted(hoursDic.items()):
	print key,value
