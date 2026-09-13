x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

# below are boolean expressions used for comparison
if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
elif x != y:
    print(f"{x} is not equal to {y}")
elif x >= y:
    print(f"{x} is greater than or equal to {y}")
elif x <= y:
    print(f"{x} is less than or equal to {y}")
elif x is y:
    print(f"{x} is {y}")
elif x is not y:
    print(f"{x} is not {y}")
else:
    print("Invalid input")