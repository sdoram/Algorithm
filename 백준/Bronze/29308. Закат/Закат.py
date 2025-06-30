russia_name = ''
russia_money = 0
for _ in range(int(input())):
    money, name, country = input().split()
    if country == 'Russia':
        if int(money) > russia_money:
            russia_money = int(money)
            russia_name = name
print(russia_name)