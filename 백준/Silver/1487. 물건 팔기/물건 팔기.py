price = {}
for _ in range(int(input())):
    key, value = map(int, input().split())
    if key not in price:
        price[key] = [value]
    else:
        price[key] += [value]

prices = []
for key in price:
    total_price = 0
    for k, value in price.items():
        if key <= k:
            for v in value:
                total_price += max(key-v, 0)
    prices.append([total_price, key])
    
lowest_price = sorted(prices, reverse=True, key=lambda x:(x[0], -x[1]))[0]

print(lowest_price[1] if lowest_price[0] != 0 else 0)