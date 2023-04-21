n = int(input())
num_list = list(map(int, input().split()))
count = n
for num in num_list:
    divisor = 2
    if num == 1:
        count -= 1
    while divisor <= round(num/2):
        if num % divisor == 0:
            count -= 1
            break
        divisor += 1
print(count)