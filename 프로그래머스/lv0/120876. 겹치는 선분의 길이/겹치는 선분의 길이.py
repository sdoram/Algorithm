def solution(lines):
    num_dict = {}
    for line in lines:
        for num in range(line[0],line[1]):
            if not num in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
    return sum([1 for num in num_dict.values() if num != 1])