a_burger = int(input())
b_burger = int(input())
c_burger = int(input())
a_drink = int(input())
b_drink = int(input())

if a_burger <= b_burger and a_burger <= c_burger:
    burger = a_burger
elif b_burger <= a_burger and b_burger <= c_burger:
    burger = b_burger
else:
    burger = c_burger

if a_drink <= b_drink:
    drink = a_drink
else:
    drink = b_drink

print(burger + drink - 50)
