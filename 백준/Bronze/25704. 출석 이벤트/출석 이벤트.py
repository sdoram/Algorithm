N = int(input())
P = int(input())
answer = []
if N >= 20:
    answer.append(int(P * 0.75))
if N >= 15:
    answer.append(P - 2000)
if N >= 10:
    answer.append(int(P * 0.9))
if N >= 5:
    answer.append(P - 500)
else:
    answer.append(P)
print(min(answer) if min(answer) > 0 else 0)
