num = list(map(int, input().split()))
print(1 if num.count(1) > num.count(2) else 2)