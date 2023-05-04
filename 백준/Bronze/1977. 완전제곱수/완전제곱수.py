M = int(input())
N = int(input())
num_list = [num*num for num in range(1, 101)]
answer_list = []
for num in range(M, N+1):
    if num in num_list:
        answer_list.append(num)
if answer_list == []:
    print(-1)
else:
    print(sum(answer_list))
    print(answer_list[0])