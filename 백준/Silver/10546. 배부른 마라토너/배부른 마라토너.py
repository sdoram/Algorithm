import sys

input = sys.stdin.readline

marathoner_dict = {}

for _ in range(int(input())*2-1):
    name = input().rstrip()
    if name not in marathoner_dict:
        marathoner_dict[name] = 1
    elif name in marathoner_dict and marathoner_dict[name] == 0:
        marathoner_dict[name] += 1
    else:
        marathoner_dict[name] -= 1

print(*[key for key, value in marathoner_dict.items() if value != 0])

