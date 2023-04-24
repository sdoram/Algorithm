a = int(input())
count = 1
answer = 0
while count < a:
    num = count
    for n in str(count):
        num += int(n)
    if num == a:
        answer = count
        break
    count += 1
print(answer)
