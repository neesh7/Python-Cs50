x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x >= y and x <= y:
    print("x is equal to y")
else:
    print("x is not equal to y")

w = [1, 2, 3, 4, 5]
if x not in w:
    print("x is not in w array")
else:
    print("x is in w array")