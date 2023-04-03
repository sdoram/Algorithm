A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A+B) % C)  # 13 나누기 4 몫은 1
print(((A % C)+(B % C)) % C)  # (몫 1) + (몫 0) % 4는 1남지
print((A*B) % C)  # 40 나누기 4는 몫 0
print((A % C)*(B % C) % C)  # (몫 1)*(몫 0) = 0 나누기 4 =0
