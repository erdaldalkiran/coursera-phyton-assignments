fileName = raw_input('Please enter the file to open? ')
if len(fileName) < 1 : fileName = 'mbox-short.txt'

fHandle = None
try:
	fHandle = open(fileName)
except:
	print 'Please enter an existing file name'
	quit()
	
wordsCount = {}
for line in fHandle:
	if line.startswith('From '):
		word = line.split()[1]
		wordsCount[word] = wordsCount.get(word, 0) + 1

fHandle.close()

largestCount = -1
largestKey = None
for key,value in wordsCount.items():
	if value > largestCount:
		largestKey = key
		largestCount = value
		
print largestKey, largestCount


