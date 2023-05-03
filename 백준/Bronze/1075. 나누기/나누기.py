N = int(input())
F = int(input())
for n in range(100):
    if (N//100*100+n) % F == 0:
        if n < 10:
            print('0'+str(n))
        else:
            print(str(n))
        break