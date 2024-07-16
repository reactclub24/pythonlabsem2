# Write a program to find the product of two matrices [A]mxp and [B]pxr
import random

print('Enter the values of m, p, r ')
m = int(input())
p = int(input())
r = int(input())
A = [[random.random() for row in range(m)] for col in range(p)]
B = [[random.random() for row in range(p)] for col in range(r)]
C = [[random.random() for row in range(m)] for col in range(r)]
print('Enter the elements of matrix A ')
for i in range(m):
    for j in range(p):
        A[i][j] = int(input())

print('Enter the elements of matrix B ')
for i in range(p):
    for j in range(r):
        B[i][j] = int(input())
print('The product of matrices A and B is ')
for i in range(m):
    for j in range(r):
        C[i][j] = 0
    for k in range(p):
        C[i][j] = C[i][j] + A[i][k] * B[k][j]
    print(C[i][j])