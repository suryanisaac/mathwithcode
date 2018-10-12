# Program to find the value of A when C and B are given

import math

a = int(input("Enter the Value of A: "))

b = int(input("Enter the Value of B: "))

ans = a ** 2 + b ** 2

c = math.sqrt(ans)

print("The Value of C is", c)
