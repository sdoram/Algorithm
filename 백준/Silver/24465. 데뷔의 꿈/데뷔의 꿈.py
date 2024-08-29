import sys

input = sys.stdin.readline

zodiac_sign = {1: [[1, 20], [2, 18]],
               2: [[2, 19], [3, 20]],
               3: [[3, 21], [4, 19]],
               4: [[4, 20], [5, 20]],
               5: [[5, 21], [6, 21]],
               6: [[6, 22], [7, 22]],
               7: [[7, 23], [8, 22]],
               8: [[8, 23], [9, 22]],
               9: [[9, 23], [10, 22]],
               10: [[10, 23], [11, 22]],
               11: [[11, 23], [12, 21]],
               12: [[12, 22], [1, 19]]}
member_dict = {i:'' for i in range(1,13)}
applicant_list = []

for _ in range(7):
    member = list(map(int, input().split()))
    for key, value in zodiac_sign.items():
        if member[0] == value[0][0] and member[1] >= value[0][1]:
            member_dict[key] = 'member'
        elif member[0] == value[1][0] and member[1] <= value[1][1]:
            member_dict[key] = 'member'

for _ in range(int(input())):
    applicant = list(map(int, input().split()))
    for key, value in zodiac_sign.items():
        if applicant[0] == value[0][0] and applicant[1] >= value[0][1] and 'member' not in member_dict[key]:
            applicant_list.append(applicant)
        elif applicant[0] == value[1][0] and applicant[1] <= value[1][1] and 'member' not in member_dict[key]:
            applicant_list.append(applicant)
            
if applicant_list:
    for applicant in sorted(applicant_list, key=lambda x:(x[0], x[1])):
        print(' '.join(map(str, (applicant))))
else:
    print('ALL FAILED')