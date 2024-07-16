# Write a program that asks the user to enter a series of positive numbers
# The user should enter a negative number to signal the end of the series
# and the program should display the numbers in order and their sum.
import random

print('Enter a series of positive numbers')
print('Enter a negative number to signal the end of the series')
total = 0
series = []
keep_going = 'y'
while keep_going == 'y':
    x = int(input())  # reading input and convert to integer

    # check for the given number is negative
    if x >= 0:
        total = total + x
    series.append(x)  # add new number to the list
    else:
    keep_going = 'n'

# Sorting list of elements in order
series.sort()
print('Entered series is', series)
print('Sum of series is', total)
# Reversing list of elements
series.reverse()
print('Entered series in reverse order is', series)