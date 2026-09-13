def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Macha chai"
    yield "Oolong chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chain_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("stall is closed so no more chai")

stall = chain_stall()
print(next(stall))
stall.close() # Always close your generator