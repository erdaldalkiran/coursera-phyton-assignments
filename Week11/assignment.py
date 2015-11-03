import re

total = 0
fileHandle = open('regex_sum_189573.txt')
for line in fileHandle:
	numbersInLine = re.findall('[0-9]+', line)
	for	number in numbersInLine:
		total += int(number)
	
print total 