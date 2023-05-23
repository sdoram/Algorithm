from collections import deque

N, K = map(int, input().split())
deque_list = deque([n for n in range(1, N + 1)])
answer = []
for _ in range(N):
    deque_list.rotate(-K + 1)
    answer.append(deque_list.popleft())
print(f'<{", ".join(map(str, answer))}>')