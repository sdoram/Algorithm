two = 0
money = int(input())
min_answer = -1
while money >= 0:
    if money % 5 == 0:
        min_answer = money // 5 + two
        break
    money -= 2
    two += 1
print(min_answer)
