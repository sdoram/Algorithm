for _ in range(int(input())):
    x = int(input())
    print(''.join([str(x), ' is even']) if x % 2 == 0 else ''.join([str(x), ' is odd']))