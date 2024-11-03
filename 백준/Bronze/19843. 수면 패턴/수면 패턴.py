week = ['','Mon', 'Tue', 'Wed', 'Thu', 'Fri']
T, N = map(int, input().split())
for _ in range(N):
    D1, H1, D2, H2 = input().split()
    H1, H2 = int(H1)+24*week.index(D1), int(H2)+24*week.index(D2)
    T -= H2 - H1
# T가 49 이상이면 48시간을 자도 목표시간을 채울 수 없음
# T가 48~1이라면 48~1시간을 자야함
# T가 음수라면 잠을 자지 않아도 충분함
print(-1 if T >= 49 else T if T > 0 else 0)