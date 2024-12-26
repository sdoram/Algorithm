A = int(input())
B = int(input())
C = int(input())
number_dict = {str(i):0 for i in range(10)}

for i in str(A*B*C):
    number_dict[i] += 1

for value in number_dict.values():
    print(value)