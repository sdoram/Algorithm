five_num = 0
a = int(input())
min_answer = -1
for _ in range(a):
    kg = a
    kg -= 5*five_num
    if kg < 0:
        break
    three = kg // 3
    if kg > 2 and (kg % 3 == 0 or kg % 5 == 0):
        current_answer = five_num+three
        if min_answer < 0:
            min_answer = current_answer
        elif min_answer > 0 and min_answer > current_answer:
            min_answer = current_answer
    five_num += 1
print(min_answer)