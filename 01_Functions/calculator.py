# using Integer inputs and arithmetic operators
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print(f"Sum of {x} and {y} is {x+y}")
# print(f"Difference of {x} and {y} is {x-y}")
# print(f"Product of {x} and {y} is {x*y}")
# print(f"Division of {x} and {y} is {x/y}")
# print(f"Integer Division of {x} and {y} is {x//y}")
# print(f"Remainder of {x} and {y} is {x%y}")
# print(f"{x} raised to the power {y} is {x**y}")

# using Float inputs and arithmetic operators
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
sum = x + y
print(f"Sum of {x} and {y} is {round(sum):,}") # rounding off to 2 decimal places and adding comma as thousand separator


divide = x / y
print(f"Division of {x} and {y} is {divide:.2f}") # rounding off to 2 decimal places using :.2f format specifier without changing the actual value of divide variable