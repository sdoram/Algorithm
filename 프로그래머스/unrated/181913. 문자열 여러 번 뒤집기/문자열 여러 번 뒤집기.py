def solution(my_string, queries):
    for s,e in queries:
        word = my_string[s:e+1]
        my_string = my_string[:s]+word[::-1]+my_string[e+1:]
    return my_string