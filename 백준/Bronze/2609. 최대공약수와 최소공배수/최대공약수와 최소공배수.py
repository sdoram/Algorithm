a, b = map(int, input().split())
LCM = 1
while True:
    for num in range(a if a >= b else b, 0, -1):
        if a % num == 0 and b % num == 0:
            a, b = a//num, b//num
            LCM *= num
            continue
    break
print(LCM)
print(LCM * a * b)