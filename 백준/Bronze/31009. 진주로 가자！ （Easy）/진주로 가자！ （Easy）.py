transportation_dict = {}
for _ in range(int(input())):
    transport = list(input().split())
    transportation_dict[transport[0]] = int(transport[1])
print(transportation_dict['jinju'])
print(len([1 for value in transportation_dict.values() if value > transportation_dict['jinju']]))