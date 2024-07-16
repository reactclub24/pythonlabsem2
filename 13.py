# Write a series of random numbers to a file from 1 to n and display.
import random
n = int(input('Enter the value of n '))
try :
 # open file in write mode
 fp = open('msc.txt','w')
 print('Name of the file is',fp.name)
 for i in range(n) :
 num = random.randrange(1, n)
 fp.write(str(num)+' ')
 fp.close()
except IOError :
 print('There is an error in file operations')
 sys.exit()
try :
 # Open file in read mode
 fp = open('msc.txt','r')
 print(fp.read())
 fp.close()
except IOError :
 print('There is an error in file operations')
 sys.exit()