# fname = raw_input("Enter file name: ")
# try:
# 	with open(fname) as fileHandle:
# 		for line in fileHandle:
# 			print line.rstrip().upper()
# except:
# 	print 'File', fname, 'not found'

fname = raw_input("Enter file name: ")
try:
	fileHandle = open(fname, 'r')
	for line in fileHandle:
		print line.rstrip().upper()
	fileHandle.close()
except:
	print 'File', fname, 'not found'