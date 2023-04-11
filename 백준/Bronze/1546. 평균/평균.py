n = int(input())
test_num = input().split()
total_score = 0
best_score = int(test_num[0])
for idx, num in enumerate(test_num):
    num = int(num)
    test_num[idx] = num
    if num > best_score:
        best_score = num

for num in test_num:
    total_score += num / best_score*100
answer = total_score / n
print(answer)