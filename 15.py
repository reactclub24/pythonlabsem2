#Write a program to analyze the contents of two text files
# using set operations (union, intersection, difference).
#error hai ismme
try:
    fp1 = open('first.txt', 'r')

    myset1 = set('')
    repeat1 = set('')
    while True:
        line = fp1.readline()
        if line == '':
            break
        else:
            wordlist = line.split()
            for word in wordlist:
                if word in myset1:
                    repeat1.add(word)
                else:
                    myset1.add(word)

    fp1.close()

except IOError:
    print('There is an error in file operations')
    sys.exit()

try:
    fp2 = open('second.txt', 'r')

    myset2 = set('')
    repeat2 = set('')
    while True:
        line = fp2.readline()
        if line == '':
            break
        else:
            wordlist = line.split()
            for word in wordlist:
                if word in myset2:
                    repeat2.add(word)
                else:
                    myset2.add(word)

    fp2.close()

except IOError:
    print('There is an error in file operations')
    sys.exit()

print('In first file')
print('Repeated  word list :\n', repeat1)
print('Unique word list :')
unique1 = myset1.difference(repeat1)
print(unique1)
print('In second file')
print('Repeated  word list :\n', repeat2)
print('Unique word list :')
unique2 = myset2.difference(repeat2)
print(unique2)
print('Comparing first file and second file')
print('Repeated  word list :'),
repeat = repeat1.union(repeat2)
print(repeat)
print('Unique word list :')
unique = unique1.difference(unique2)
print(unique)
print('Common word list :')
common = unique1.intersection(unique2)
print(common)