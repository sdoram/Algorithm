for hero in [input() for _ in range(int(input()))]:
    h = hero.lower()
    print(f"{hero} is {'GOOD' if h.count('g') > h.count('b') else 'A BADDY' if h.count('b') > h.count('g') else 'NEUTRAL'}")