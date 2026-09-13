import random


# class method
class Hat:
    # class variables
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod # with class method we use cls keyword to represent it is calling a class variables
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name,"is in", house)



# In case of classmethod we don't need to intanciate a object instead we can directly call the call to take actions.
Hat.sort("Harry")