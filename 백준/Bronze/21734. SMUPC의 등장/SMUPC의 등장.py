for S in input():
    print(S * sum([int(s) for s in str(ord(S))]))