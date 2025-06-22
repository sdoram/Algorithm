H, M, S = map(int, input().split())
total_time = H * 3600 + M * 60 + S + 1
if total_time == 86400:
    print('00:00:00')
else:
    print(f'{str(total_time // 3600).zfill(2)}:{str(total_time % 3600 // 60).zfill(2)}:{str(total_time % 3600 % 60).zfill(2)}')