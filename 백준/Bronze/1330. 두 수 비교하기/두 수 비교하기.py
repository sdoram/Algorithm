# if문 사용
# A가 크면 >
# B가 크면 <
# 같으면 ==

A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')