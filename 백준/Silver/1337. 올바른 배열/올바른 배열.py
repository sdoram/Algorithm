array = sorted([int(input()) for _ in range(int(input()))])
array_dict = {}

for arr in array:
    for a in range(arr, arr+5):
        if a not in array_dict:
            array_dict[a] = 4
        else:
            array_dict[a] -= 1
            
print(min(array_dict.values()))