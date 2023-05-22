birthday_list = [list(input().split()) for _ in range(int(input()))]
for n in range(1, 4):
    birthday_list = sorted(birthday_list, key=lambda x: int(x[n]))
print(birthday_list[-1][0])
print(birthday_list[0][0])