from sys import stdin

q_list = []
for _ in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if command[0] == "push":
        q_list.append(int(command[1]))
    elif command[0] == "size":
        print(len(q_list))
    elif command[0] == "empty":
        print(0 if q_list else 1)
    try:
        if command[0] == "pop":
            print(q_list.pop(0))
        elif command[0] == "front":
            print(q_list[0])
        elif command[0] == "back":
            print(q_list[-1])
    except IndexError:
        print(-1)