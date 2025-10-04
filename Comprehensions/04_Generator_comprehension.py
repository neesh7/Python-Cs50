# Generators in Python are a powerful way to create iterators without storing 
# the entire sequence in memory. They let you yield values one at a time, 
# making your code more efficient, lazy, 
# and scalable — especially when dealing with large datasets or streams.

# Generator comprehension Syntax 
# (expression loops conditions) - it works like stream instead of clogging memory at once

daily_sales = [5,10,12,15,19,23,28]
total_cups = sum(sale for sale in daily_sales if sale > 3) # this is a memory efficent code
print(total_cups)