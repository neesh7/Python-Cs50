from calculator import square

print("running tests !")

def main():
    test_square()


# basic level
# def test_pow():
#     print("Inside testing function ! ")
#     if power_num(2,2) != 4:
#         print(" 2 squared is not 4")
#     if power_num(3,3) != 9:
#         print(" 3 squared is not 9")

###################### Using assert to do testing  ###########################
def test_square():
    print("Inside testing function ! ")
    for i in range(10):
        try:
            assert square(i) == i**i
            print(f"tests passed for value of i : {i}")
        except AssertionError:
            print(f" {i} squared is not {i**i}")
        

if __name__=="__main__":
    main()