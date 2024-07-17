for i in range(1, int(input())+1):
    input()
    price_dict = {}
    price = list(map(int, input().split()))
    new_price = []
    
    for p in price:
        if p not in price_dict:
            price_dict[p] = 1
        else:
            price_dict[p] += 1
    
    for p in price:
        if int(p * 0.75) in price_dict and price_dict[int(p * 0.75)] > 0:
            price_dict[int(p * 0.75)] -= 1
            price_dict[p] -= 1
            new_price.append(int(p * 0.75))
    print(f"Case #{i}: {' '.join(map(str, new_price))}")