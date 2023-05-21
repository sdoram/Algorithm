c_score = 100
s_score = 100
for _ in range(int(input())):
    c, s = map(int, input().split())
    if c > s:
        s_score -= c
    if c < s:
        c_score -= s
print(c_score)
print(s_score)