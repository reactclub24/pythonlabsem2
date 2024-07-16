 Write a program that opens a specified text file and
# then displays a list of all the unique words found in the file.
# Store each word as an element of a set.
try :
# open a text file in read mode
fp = open('msc.txt','r')
myset = set('')
repeat = set('')
while True :
line = fp.readline()
if line == '' :
break
else :
wordlist = line.split()
for word in wordlist :
if word in myset :
repeat.add(word)
else :
myset.add(word)
fp.close()
except IOError :
print('There is an error in file operations')
sys.exit()
unique = myset.difference(repeat)
print(unique)