name = input("What's your name? ").capitalize()

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# elif name == "Luna":
#     print("Ravenclaw")
# else:
#     print("Who???")

# using switch case or match case (python 3.10+)
match name:
    case "Harry" | "Neville" | "Hermione": # basically the pipe operator (|) works as OR operator
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case _:
        print("Who???")