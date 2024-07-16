# Write a program to display two random numbers that are to be added,
# the program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect, a message showing the correct answer.
import random
print('Addition of two random integers between 0 and 1000')
x = random.randrange(1000)
y = random.randrange(1000)
sum = x+y
z = int(input('Enter your guess '))
if sum==z :
 print('Congratulations, you have entered correct answer')
elif sum>z :
 print('You have entered low number')
 print('Correct answer is',sum)
else :
 print('You have entered high number')
 print('Correct answer is',sum)