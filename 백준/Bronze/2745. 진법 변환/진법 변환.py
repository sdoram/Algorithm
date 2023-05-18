N, B = input().split()
B = int(B)
ANSWER = 0
for idx, num in enumerate(N[::-1]):
    if 64 < ord(num) < 91:
        ANSWER += (ord(num) - 55) * pow(B, idx)
    else:
        ANSWER += int(num) * pow(B, idx)
print(ANSWER)