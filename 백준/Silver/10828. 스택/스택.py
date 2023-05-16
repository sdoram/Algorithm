from sys import stdin

stack_list = []
for _ in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if command[0] == "push":
        stack_list.append(int(command[1]))
    elif command[0] == "size":
        print(len(stack_list))
    elif command[0] == "empty":
        print(0 if stack_list else 1)
    try:
        if command[0] == "pop":
            print(stack_list.pop())
        elif command[0] == "top":
            print(stack_list[-1])
    except IndexError:
        print(-1)
