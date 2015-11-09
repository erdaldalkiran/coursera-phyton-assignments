import re

spamConfidences = []

fname = raw_input("Enter file name: ")

try:
	fileHandle = open(fname, 'r')
except:
	print 'File', fname, 'not found'
	exit()

for line in fileHandle:
	spamConfidencesStringList = re.findall('^X-DSPAM-Confidence:\s+(0[.][0-9]+)', line)
	if len(spamConfidencesStringList) > 0:
		spamConfidences.append(float(spamConfidencesStringList[0]))

if len(spamConfidences) > 0:
	print 'Average spam confidence:', sum(spamConfidences) / len(spamConfidences)
else:
	print 'No Spam Confidence Found'

fileHandle.close()