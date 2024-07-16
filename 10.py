# Write recursive and non-recursive functions to display prime numbers from 2 to n
def main():
    n = int(input('Enter a positive integer '))
    print('Rec: Prime numbers are')
    for i in range(2, n + 1):
        if prime_rec(2, i, 2) != 0:
            print(i)

    print('Non_Rec: Prime numbers are')
    for i in range(2, n + 1):
        if prime_nonrec(i) != 0:
            print(i)


# Define Recursive function
def prime_rec(fact, x, y):
    if (fact == 2) & (x == y):
        return x
    elif x % y == 0:
        return prime_rec(fact + 1, x, y + 1)
    elif fact > 2:
    return 0
    else:
    return prime_rec(fact, x, y + 1)


# Define Non-recursive function
def prime_nonrec(x):
    for i in range(2, x):
        if x % i == 0:
            return 0


# Call main function
main()