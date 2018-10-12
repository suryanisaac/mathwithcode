# Program to find hypotenuse when legs are given

import math

leg1 = int(input("Enter the Length of the First Leg: "))

leg2 = int(input("Enter the Length of the Second Leg: "))

hypotenuse2 = (leg1 ** 2) + (leg2 ** 2)

hypotenuse = math.sqrt(hypotenuse2)

print(hypotenuse2, "is the Square of the Hypotenuse of the given legs")
 # print(hypotenuse)