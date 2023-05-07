def get_gcd(A, B):
    if A < B:
        A, B = B, A
    if A % B == 0:
        return B
    if A % B != 0:
        gcd = A % B
        while B % gcd != 0:
            B, gcd = gcd, B % gcd
    return gcd


for _ in range(int(input())):
    A, B = map(int, input().split())
    print(A*B//get_gcd(A, B))