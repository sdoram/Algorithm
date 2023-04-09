a = int(input())
b = input().split()
c = input()
count = 0
for i in b[:a]:
    if i == c:
        count += 1
print(count)
