n, a, b = map(int, input().split())
water_list = [int(input()) for _ in range(n-1)]
if min(water_list) != a and max(water_list) == b:
    print(a)
elif max(water_list) != b and min(water_list) == a:
    print(b)
elif max(water_list) != b and min(water_list) != a:
    print(-1)
else:
    for i in range(a, b+1):
        print(i)
