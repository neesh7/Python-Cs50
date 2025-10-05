## Tuple demo
# def main():
#     student = get_student()
#     print(f"{student[0]} belongs to {student[1]}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# def get_student()   :
#     name = get_name()
#     house = get_house()

#     return (name, house) # Note by default also we return tuple and tuples are immutable


# if __name__=="__main__":
#     main()


# Same code using list because we needed mutablity
# def main():
#     student = get_student()
#     if student[0] == "padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} belongs to {student[1]}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# def get_student()   :
#     name = get_name()
#     house = get_house()

#     return [name, house] # Note by default also we return tuple and tuples are immutable


# if __name__=="__main__":
#     main()

# same example using dictionary 

def main():
    student = get_student()
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"
    print(f'{student["name"]} belongs to {student["house"]}')

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

def get_student()   :
    student = {"name": input("Name: "),
               "house": input("House: ")}

    # return student["name"], student["house"]
    return student # Dict is mutable


if __name__=="__main__":
    main()