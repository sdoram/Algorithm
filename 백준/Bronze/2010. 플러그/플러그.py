import sys
answer = 1

for _ in range(int(sys.stdin.readline())):
    answer += int(sys.stdin.readline())-1
print(answer)