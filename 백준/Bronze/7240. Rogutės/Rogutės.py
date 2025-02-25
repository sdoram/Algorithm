N, S = map(int, input().split())
speed = 0
for _ in range(N):
    if speed > S:
        speed -= 1
    speed += int(input())
print(speed)