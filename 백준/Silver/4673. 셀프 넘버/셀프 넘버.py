num_list = [num for num in range(1, 10000)]
for num in range(1, 10000):
    try:
        num_list.remove(num + sum([int(n) for n in str(num)]))
    except ValueError:
        pass
print(*num_list, sep="\n")