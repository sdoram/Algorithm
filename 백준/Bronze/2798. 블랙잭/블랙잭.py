EA, target_num = map(int, input().split())
card_num = list(map(int, input().split()))
max_num = 0
while len(card_num) > 2:
    num1 = card_num.pop()
    for num2 in range(len(card_num)):
        for num3 in range(len(card_num)):
            if num2 == num3:
                continue
            current_num = num1 + card_num[num2] + card_num[num3]
            if current_num >= max_num and current_num <= target_num:
                max_num = current_num
print(max_num)
