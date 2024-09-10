pizza = [input() for _ in range(int(input()))]
order = 0
p1 = pizza.count('1/4')
p2 = pizza.count('1/2')
p3 = pizza.count('3/4')

if p3 >= p1:
    order += p3
    p1 = 0
else:
    order += p3
    p1 -= p3
order += (p1 + 3) // 4
order += (p2 + 1) // 2
if p1 % 2 != 0 and p2 % 2 != 0:
    order -= 1
print(order)