N = int(input())
M = N
for _ in range(N):
    M -= int(input())

print("Junhee is cute!" if M < N / 2 else "Junhee is not cute!")
