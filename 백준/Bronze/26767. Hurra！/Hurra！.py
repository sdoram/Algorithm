for n in range(1, int(input())+1):
    if n % 11 == 0 and n % 7 == 0:
        print('Wiwat!')
    elif n % 11 == 0:
        print('Super!')
    elif n % 7 == 0:
        print('Hurra!')
    else:
        print(n)