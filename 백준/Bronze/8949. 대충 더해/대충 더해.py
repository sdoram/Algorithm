import sys
input = sys.stdin.readline

def roughly_plus():
    A, B = input().split()
    result = ''
    # 자리수를 맞추기 위해 앞에 0 채워넣기
    if len(A) > len(B):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))

    for i, a in enumerate(A):
        result += str(int(a) + int(B[i]))
        
    return int(result)

print(roughly_plus())