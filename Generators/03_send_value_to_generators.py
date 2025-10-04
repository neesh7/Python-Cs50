# Sending data to yield
# This is a very widely used example

def chai_customer():
    print("Welcom, what chai would you like?")
    order = yield # Basically using this yeild we are waiting for the customer to send data to yield
    while True:
        print(f"Preparing: {order}") # we execute our loop logic part here
        order = yield # and here again we go into wait mode until the caller calls agains


stall = chai_customer()
next(stall) # Start the generator

stall.send("Masala chai")
stall.send("Lemon Chai")