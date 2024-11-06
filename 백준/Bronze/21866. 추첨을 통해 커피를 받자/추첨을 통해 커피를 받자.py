score = list(map(int, input().split()))
if score[0] >= 101 or score[1] >= 101 or score[2] >= 201 or score[3] >= 201:
    print('hacker')
elif score[4] >= 301 or score[5] >= 301 or score[6] >= 401 or score[7] >= 401 or score[8] >= 501:
    print('hacker')
else:
    print('draw' if sum(score) >= 100 else 'none')