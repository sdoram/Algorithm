alpah = input()
alpah_dict = {}
for a in alpah.upper():
    if a not in alpah_dict:
        alpah_dict[a] = 1
    else:
        alpah_dict[a] += 1
sorted_dict = sorted(alpah_dict.items(), reverse=True,
                     key=lambda value: value[1])
try:
    if sorted_dict[0][1] != sorted_dict[1][1]:
        print(sorted_dict[0][0])
    else:
        print('?')
except IndexError:
    print(sorted_dict[0][0])
