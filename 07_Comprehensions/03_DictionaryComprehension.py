# Syntax {[expression] [loop] [conditional]}
# expression needs to be in Key-value format then this will be dictionary comprehension

tea_prices_inr = { 
    "MasalaChai": 40,
    "GreenTea": 50,
    "LemonTea": 200
}

# Basically 1 USD = 88 Inr approx as of now
# Naive approch or childish way
tea_prices_dollar = {}
for teas in tea_prices_inr:
    print(teas)
    prices = tea_prices_inr[teas]
    print(prices)
    prices_in_dollar = round(prices/88,2)
    tea_prices_dollar[teas] = prices_in_dollar

print(tea_prices_dollar)

# Smart approach
our_prices = {}
for tea, price in tea_prices_inr.items():
    our_prices[tea] = round(price/88,2)
print(our_prices)

# doing the conversion in single line
teas_in_dollar = { tea:round(price/88,2) for tea, price in tea_prices_inr.items()}
print("tea prices in dollar", teas_in_dollar)