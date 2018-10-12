# Program to find the value of B when A and C are given

import math

a = int(input("Enter the Value of A: "))

c = int(input("Enter the Value of C: "))

ans = c ** 2 - a ** 2

b = math.sqrt(ans)

print("The Value of B is", b)
