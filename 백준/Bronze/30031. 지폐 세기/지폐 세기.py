money = 0
for _ in range(int(input())):
    N = list(map(int, input().split()))
    if N[0] == 136:
        money += 1000
    elif N[0] == 142:
        money += 5000
    elif N[0] == 148:
        money += 10000
    else:
        money += 50000
print(money)