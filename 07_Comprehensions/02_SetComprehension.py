# Before we start with set comprehensions let's review sets first

numbers = [1,2,3,4,5,6,2,3,4] # This is list with duplicate numbers
num_sets = {1,2,3,4,5,5,6} # Duplicates not allowed, Immutable and Unordered
# print(num_sets)
# for i in num_sets:
#     print(i,end=",")

# set comprehension to store unique values only
unique_values = {unique for unique in numbers} # no condtionals filtering required as set doesn't allow duplicates by defaults
print("Unique values from list:",unique_values)


# set comprehensions - to do even, odd
even_set = {n for n in numbers if n %2==0}
print(even_set)

# Little complicated demo over nested data structures

recipes = {
    "Masala Chai": ["ginger", "bay leaves", "clove", "cardamom"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

# for ingredient in recipes.values():
#     print(ingredient)
#     for spices in ingredient:
#         print(spices)

# As above dict is a nested types we need nested loops to handle them
uniques_spices = {spices for ingredient in recipes.values() 
                            for spices in ingredient}
print(uniques_spices)