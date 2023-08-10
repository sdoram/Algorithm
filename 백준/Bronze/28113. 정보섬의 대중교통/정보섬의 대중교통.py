N, A, B = map(int, input().split())
if A > B:
    print("Subway")
elif B > A:
    print("Bus")
else:
    print("Anything")
