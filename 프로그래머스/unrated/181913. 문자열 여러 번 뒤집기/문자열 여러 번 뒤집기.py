def solution(my_string, queries):
    for i in queries:
        word = my_string[i[0]:i[1]+1]
        my_string = my_string[:i[0]]+word[::-1]+my_string[i[1]+1:]
    return my_string