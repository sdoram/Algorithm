n, k = map(int, input().split())
count = 0
time = int(input())
for _ in range(n-1):
    new_time = int(input())
    
    if time >= new_time + k:
        count += 1
    time = new_time
print(count)