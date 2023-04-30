S = int(input())
num = 0
count = 1
while True:
    num += count
    if num + count+1 > S:
        print(count)
        break
    count += 1