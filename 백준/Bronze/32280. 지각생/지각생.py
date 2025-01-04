go_to_school_dict = {'student': [],
                     'teacher': []}
for _ in range(int(input())+1):
    time, people = input().split()
    hour = int(time.split(':')[0]) * 60
    minute = int(time.split(':')[1])
    go_to_school_dict[people] += [hour + minute]

time = input().split(':')
late_time = max(go_to_school_dict['teacher'][0], int(time[0])*60 + int(time[1]))
print(len([1 for value in go_to_school_dict['student'] if value >= late_time]))