frame_list = list()
for _ in range(int(input())):
    A, B = map(int, input().split())
    frame_list.append(A*B)
print(max(frame_list))