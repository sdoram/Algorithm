import sys

input = sys.stdin.readline

N, M = map(int, input().split())

team_dict = {i:[] for i in range(1, N+1)}

while True:
    num, student = input().split()
    if num == '0' and student == '0':
        break
    if M > len(team_dict[int(num)]):
        team_dict[int(num)].append(student)
        
for key, value in team_dict.items():
    if key % 2 != 0:
        for v in sorted(value, key= lambda x:(len(x), x)):
            print(key, v)

for key, value in team_dict.items():
    if key % 2 == 0:
        for v in sorted(value, key= lambda x:(len(x), x)):
            print(key, v)
