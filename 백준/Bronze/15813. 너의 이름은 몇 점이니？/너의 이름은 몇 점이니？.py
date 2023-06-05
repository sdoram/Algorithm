import string

N = int(input())
alpha_list = string.ascii_uppercase
print(sum([alpha_list.index(w) + 1 for w in input()]))
