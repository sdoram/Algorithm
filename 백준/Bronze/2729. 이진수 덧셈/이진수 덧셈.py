for _ in range(int(input())):
    X, Y = input().split()
    print(bin(int(X, 2) + int(Y, 2))[2:])