# Program to find the value of A when C and B are given

import math

b = int(input("Enter the Value of B: "))

c = int(input("Enter the Value of C: "))

ans = c ** 2 - b ** 2

a = math.sqrt(ans)

print("The Value of A is", a)
