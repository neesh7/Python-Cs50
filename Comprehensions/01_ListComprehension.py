# Syntax [[expression] [loop] [conditional]]
# [expression for item in iterable if condition]

# Let's say we have a list of numbers in list below
numbers = [1,2,3,4,5,6,7,8,9]

# we want to filter even number in even_no list and odd number in odd_no list

# Normal code/ approach
even_no = []
odd_no = []

for i in numbers:
    if i%2 == 0: 
        even_no.append(i)
    else:
        odd_no.append(i)

print("even_no: ",even_no)
print("odd_no: ",odd_no)

# Using List comprehensions we can cut down whole logic in single line
even = [ num for num in numbers if num %2 ==0]
odd = [num for num in numbers if num %2 !=0]

print("even:",even)
print("odd",odd)