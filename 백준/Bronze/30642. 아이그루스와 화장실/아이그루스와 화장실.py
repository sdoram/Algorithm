N = int(input())
M = input()
K = int(input())

if K == 1:
    print(1 if M == 'annyong' else 2)
else:
    if M == 'annyong':
        print(K if K % 2 != 0 else K-1)
    else:
        print(K if K % 2 == 0 else K-1)