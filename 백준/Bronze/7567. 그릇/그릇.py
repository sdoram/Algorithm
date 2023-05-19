BOWL = input()
NUM = 0
for i, b in enumerate(BOWL, -1):
    if i >= 0 and b == BOWL[i]:
        NUM += 5
    else:
        NUM += 10
print(NUM)