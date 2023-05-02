N = int(input())
call = list(map(int, input().split()))
M = 0
Y = 0
for c in call:
    Y += (c // 30+1) * 10
    M += (c // 60+1) * 15
if M < Y:
    print(f'M {M}')
elif Y == M:
    print(f'Y M {M}')
else:
    print(f'Y {Y}')
