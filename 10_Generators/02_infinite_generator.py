# An infinite generator is a function that never exhausts its values. 
# It keeps yielding new results forever, or until you explicitly stop it.
def infinit_gen():
    count = 1
    while True:
        yield f"Refil #{count}"
        count +=1

refill = infinit_gen()
for _ in range(3):
    print(next(refill))