import sys

input = sys.stdin.readlines

number_list = [list(map(int, num.rstrip().split())) for num in input()]
number_dict = {}

for numbers in number_list:
    for num in numbers:
        for n in range(1, int(num**0.5)+1):
            if num % n == 0:
                if num // n not in number_dict:
                    number_dict[num//n] = [num]
                else:
                    number_dict[num//n] += [num]
                if n != num//n:
                    if n not in number_dict:
                        number_dict[n] = [num]
                    else:
                        number_dict[n] += [num]

print(max([key for key, value in number_dict.items() if len(value) >= 2]))