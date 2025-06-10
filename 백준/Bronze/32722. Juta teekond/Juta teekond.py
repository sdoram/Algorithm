x = int(input())
y = int(input())
z = int(input())

check = False
if x == 1 or x == 3:
    if y == 6 or y == 8:
        if z == 2 or z == 5:
            check = True
            
print('JAH' if check else 'EI')