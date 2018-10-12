# Program to find if a given set of numbers are pythagorean triplets

num1 = int(input("Enter The Largest Number: "))

num2 = int(input("Enter The Second Number: "))

num3 = int(input("Enter The Third Number: "))

pt = True

n1s = num1 * num1

n2s = num2 * num2

n3s = num3 * num3

if (n1s == n2s + n3s):

    pt = True

    print("The Numbers are Pythagorean Triplets")

else:

    pt = False

    print("The Numbers are not Pythagorean Triplets")
