T = int(input())
if T % 10:
    print(-1)
else:
    a = 300
    a_count = 0
    b = 60
    b_count = 0
    c = 10
    c_count = 0
    while T:
        if T >= a:
            T -= a
            a_count += 1
        elif T >= b:
            T -= b
            b_count += 1
        elif T >= c:
            T -= c
            c_count += 1
    print(f"{a_count} {b_count} {c_count}")
