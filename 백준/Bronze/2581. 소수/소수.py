import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime_number_list = []
for num in range(M, N+1):
    for i in range(1, num):
        if i != 1 and num % i == 0:
            break
        if i+1 == num:
            prime_number_list.append(i+1)
if prime_number_list != []:
    print(sum(prime_number_list))
    print(prime_number_list[0])
else:
    print(-1)