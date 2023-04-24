x, y, w, h = map(int, input().split())
num_list = [x, w-x, y, h-y]
num_list.sort()
print(num_list[0])