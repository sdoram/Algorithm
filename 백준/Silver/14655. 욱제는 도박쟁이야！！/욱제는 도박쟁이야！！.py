int(input())

ANSWER = list(map(int, input().split()))
ANSWER.extend(map(int, input().split()))
print(sum(map(abs, ANSWER)))