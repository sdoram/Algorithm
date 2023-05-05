import sys
def solution(num_list):
    count = 1
    while True:
        answer = 0
        for num in num_list:
            if count % num == 0:
                answer += 1
            if answer == 3:
                return count
        count += 1


print(solution(list(map(int, sys.stdin.readline().split()))))
