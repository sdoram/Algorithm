import string

for _ in range(int(input())):
    ascii_dict = {key: True for key in string.ascii_uppercase}
    S = list(input())
    for s in S:
        ascii_dict[s] = False
    print(sum([ord(key) for key, value in ascii_dict.items() if value]))
