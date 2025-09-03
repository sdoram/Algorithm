N = input()
if '7' in N:
    print(3 if int(N) % 7 == 0 else 2)
else:
    print(1 if int(N) % 7 == 0 else 0)