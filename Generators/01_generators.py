def serve_chain():
    yield "Cup1 : Masala chai"
    yield "Cup2 : Elaichi chai"
    yield "Cup3 : Ginger chai"

stall = serve_chain()
# print(stall)
# for chai_types in stall:
#     print(chai_types)

print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall)) # gives errors