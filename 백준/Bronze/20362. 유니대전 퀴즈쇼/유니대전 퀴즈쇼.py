N, S = input().split()
name = []
answer = []
count = 0
for _ in range(int(N)):
    n, a = input().split()
    name.append(n)
    answer.append(a)
correct_answer = answer[name.index(S)]
for i, a in enumerate(answer):
    if name[i] == S:
        break
    elif a == correct_answer:
        count += 1
print(count)  