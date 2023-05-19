total_score = []
for _ in range(int(input())):
    dice_list = sorted(list(map(int, input().split())))
    if dice_list[0] == dice_list[2]:
        total_score.append(dice_list[0] * 1000 + 10000)
    elif dice_list[0] == dice_list[1]:
        total_score.append(dice_list[1] * 100 + 1000)
    elif dice_list[2] == dice_list[1]:
        total_score.append(dice_list[1] * 100 + 1000)
    else:
        total_score.append(dice_list[2] * 100)
print(max(total_score))