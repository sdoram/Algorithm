three = 0
kg = int(input())
min_answer = -1
while kg >= 0:
    if kg % 5 == 0:
        min_answer = kg//5+three
        break
    kg -= 3
    three += 1
print(min_answer)