# Write a program to find the factorial positive integer
def main():
 n = int(input('Enter a positive integer '))
 print('Rec: Factorial value is',fact_rec(n))
 print('Non-Rec: Factorial value is',fact_nonrec(n))
# Define Recursive function
def fact_rec(x):
 if x==1:
 return 1
 else:
 return x*fact_rec(x-1)
# Define Non-recursive function
def fact_nonrec(x):
 fact = 1
 for i in range(1, x+1):
 fact = fact*i
 return fact
# Call main function
main()
