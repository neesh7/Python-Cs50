# import random


# toss = random.choice(['Heads','Tails'])
# print(toss)
# tossing a coin

# other appraoch if you want to import choice only.
from random import choice

toss = choice(['Heads','Tails'])
print(toss)

import random


a, b = 1, 10
random_number = random.randint(a,b)
print(random_number)

cards = ["ace", "jack", "king", "queen"]
random.shuffle(cards)
for card in cards:
    print(card)