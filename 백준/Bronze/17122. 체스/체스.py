import sys, string
input = sys.stdin.readline

def check():
    black = [True, False, True, False, True, False, True, False]
    white = [False, True, False, True, False, True, False, True]
    alphabet = list(string.ascii_uppercase)
    
    for _ in range(int(input())):
        a, b = input().split()
        b = int(b)
        a_location = black[alphabet.index(a[0])] if int(a[1]) % 2 != 0 else white[alphabet.index(a[0])]
        # 짝수면 black시작
        b_location = black[(b-1) % 8] if (b-1) // 8 % 2 == 0 else white[(b-1) % 8]
        if a_location == b_location:
            print('YES')
        else:
            print('NO')
            
check()