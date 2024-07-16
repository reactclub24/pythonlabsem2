# Write a program to find the largest three integers using if-else
print('Enter any three integers ')
x = int(input('Enter first integer '))
y = int(input('Enter second integer '))
z = int(input('Enter third integer '))
if x>y :
    if x>z :
     large = x
    else:
     large = z

     if y>z :
      large=y
     else:
      large = z
print('Largest of entered three integers is',large)