a, b = map(int, input().split())
c = input().split()
d = []
answer = ''
for i in c[:a]:
    if int(i) < b:
        d.append(i)
answer = ' '.join(d)
print(answer)