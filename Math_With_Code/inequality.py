# Program to find if a set of numbers can form a 90˚ triangle

AB = int(input("Enter The Value of AB: "))

BC = int(input("Enter The Value of BC: "))

CA = int(input("Enter The Value of CA: "))

n1 = AB + BC

n2 = AB + CA

n3 = BC + CA

v1 = False

v2 = False

v3 = False

if n1 > CA:

    v1 = True

else:

    v1 = False

if n2 > BC:

    v2 = True

else:

    v2 = False

if (n3 > AB):

    v3 = True

else:

    v3 = False

if v1 and v2 and v3 == True:

    print("The Set of numbers CAN form a 90˚ Triangle")

else:

    print("The Set of numbers CANNOT form a 90˚ Triangle")
