import string

N = int(input())
alpha_list = string.ascii_uppercase
ANSWER = 0
for w in input():
    ANSWER += alpha_list.index(w) + 1

print(ANSWER)