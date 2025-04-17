input()
N = input().split()
A = input().split()
for ingredient in N:
    if (N+A).count(ingredient) == 1:
        print(ingredient)
        break