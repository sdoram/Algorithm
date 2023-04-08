total = int(input())
buy_num = int(input())
count = 0
answer = 0

while buy_num > count:
    price, number = input().split()
    price = int(price)
    number = int(number)
    answer += price * number
    count += 1

if total == answer:
    print('Yes')
else:
    print('No')
