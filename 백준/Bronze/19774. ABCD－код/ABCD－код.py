for _ in range(int(input())):
    x = input()

    print('YES' if (int(x[:2])**2 + int(x[2:])**2) % 7 == 1 else 'NO')