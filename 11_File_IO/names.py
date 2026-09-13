names = []

for _ in range(3):
    names.append(input("What is your name? "))
# name=input('What is your name')
print(f"Hello {names}")
for i in sorted(names):
    print(f"hello, {i}")