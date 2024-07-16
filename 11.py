# Write a function that accepts two arguments: a list and a number n.
# The function displays all of the numbers in the list that are greater than n.
def main():
    print('Enter a list of positive numbers')
    print('Enter a negative number to signal the end of the list')
    numbers = []
    keep_going = 'y'
    while keep_going == 'y':
        x = int(input())
    if x >= 0:
        numbers.append(x)
    else:
        keep_going = 'n'

    n = int(input('Enter the value of n '))
    print('Display the numbers in the list')
    display_list(numbers, n)


# Function definition
def display_list(given_list, n):
    for num in given_list:
        if num > n:
            print(num)


# Calling main function
main()

print('its been committed ')