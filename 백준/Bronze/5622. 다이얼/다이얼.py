dial_num = [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K',
                                                                   'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']
call = input()
time = 0
for num in call:
    count = 1
    for dial in dial_num:
        count += 1
        if num in dial:
            time += count
print(time)