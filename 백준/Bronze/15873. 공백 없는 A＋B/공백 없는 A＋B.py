NUM = input()
if NUM[1] == '0':
    A, B = int(NUM[:2]), int(NUM[2:])
else:
    A, B = int(NUM[:1]), int(NUM[1:])
print(A+B)