ls = [1,2,3,4,5]

# lambda arguments: expression
def length(ls: list) -> int:
    return len(ls)
lent = lambda ls: len(ls)
print(lent(ls))

for i in range(5):
    print(f"Hello {(lambda x: x * 2)(i)}")