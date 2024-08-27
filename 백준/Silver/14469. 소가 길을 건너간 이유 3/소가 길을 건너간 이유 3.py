time = 0

for cow in sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: x[0]):
    if time > cow[0]:
        time += cow[1]
    else:
        time = sum(cow)
print(time)