a = list(map(int, input().split()))
num = 0
for i in a:
    num += i**2
answer = num % 10
print(answer)