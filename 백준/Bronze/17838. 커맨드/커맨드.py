for _ in range(int(input())):
    command = input()
    command_dict = {}
    for c in command:
        if c not in command_dict:
            command_dict[c] = 1
        else:
            command_dict[c] += 1
    if len(command) == 7:
        if len(command_dict) == 2:
            if command[0] == command[1] == command[4]:
                print(1)
                continue
    print(0)
