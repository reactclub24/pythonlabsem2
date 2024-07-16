# Write a program to find the GCD of two positive integers
def main():
 print('Enter any two positive integers')
 m = int(input())
 n = int(input())
 gcd_rec(m, n)
 gcd_nonrec(m, n)
# Define Recursive function
def gcd_rec(x, y):
 if y==0 :
 print('Rec: GCD of given integers is',x)
 else:
 gcd_rec(y, x%y)
# Define Non-recursive function
def gcd_nonrec(x, y):
 while x%y!=0 :
 r = x%y
 x = y
 y = r
 print('Non-Rec: GCD of given integers is',y)
# Call main function
main()
