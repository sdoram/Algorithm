h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
if h2 < h1:
    h2 += 24
if s2 < s1:
    s2 += 60
    m2 -= 1
if m2 < m1:
    m2 += 60
    h2 -= 1
print(f"{str(h2-h1).zfill(2)}:{str(m2-m1).zfill(2)}:{str(s2-s1).zfill(2)}")
