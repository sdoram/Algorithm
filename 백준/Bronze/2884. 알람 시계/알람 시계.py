# 시간 구하기 24시간 기준
# 0분으로 내려가는 경우 만들기
# 0시로 내려가는 경우 23시로 만들기
H, M = input().split()
H = int(H)
M = int(M)

M = M - 45
if M < 0:
    # 60분-남은 분
    M = 60+M
    H -= 1
if H < 0:
    H = 23
print(H, M)