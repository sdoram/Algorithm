import string
alphabet = list(' '+string.ascii_uppercase)
for _ in range(int(input())):
    LIFE_SCORE = sum([alphabet.index(a) for a in input()])
    print('PERFECT LIFE' if LIFE_SCORE == 100 else LIFE_SCORE)