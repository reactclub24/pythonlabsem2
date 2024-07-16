# Write a program to print Fibonacci sequence up to given number n
def main():
    n = int(input('How many terms do you want '))
    print('Rec: Fibonacci series is')
    for i in range(n):
        print(fib_rec(i))

    print('Non_Rec: Fibonacci series is ')
    fib_nonrec(n)


# Define Recursive function
def fib_rec(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
    return fib_rec(x - 1) + fib_rec(x - 2)


# Define Non-recursive function
def fib_nonrec(x):
    f1 = 0
    f2 = 1
    print(f1)
    print(f2)
    for i in range(2, x):
        f3 = f2 + f1
    print(f3)
    f1 = f2
    f2 = f3


# Call main function
main()