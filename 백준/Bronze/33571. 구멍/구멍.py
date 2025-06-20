One = ['A', 'a', 'b', 'D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@']
S = input()
print(sum([S.count(o) for o in One], S.count('B')*2))