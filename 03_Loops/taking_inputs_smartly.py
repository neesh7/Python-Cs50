# while True:
#     n = int(input('Enter a number: '))
#     if n < 0:
#         continue
#     else:
#         break
def get_num():
    while True:
        n = int(input('Enter a number: '))
        if n > 0:
            # break
            return n
    
# for _ in range(n):
#     print('Meow')

def main():
    num = get_num()
    meow(num)

def meow(n):
    for _ in range(n):
        print('Meow')
        # print('Meow', f'Loop no {_}')

main()