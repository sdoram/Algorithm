import sys
N = int(input())
num_list = [0] * 10001
for n in range(N):
    num_list[int(sys.stdin.readline())] += 1
for n in range(10001):
    for i in range(num_list[n]):
        print(n)
