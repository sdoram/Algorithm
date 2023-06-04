N, M = map(int, input().split())
input_list = []
for _ in range(M):
    input_list.append(input().split())
    
input_list = sorted(input_list, key=lambda x: [int(x[1]), int(x[0])])
print("".join([x[2] for x in input_list]))