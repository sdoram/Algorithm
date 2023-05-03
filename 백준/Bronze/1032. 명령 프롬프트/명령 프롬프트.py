for _ in range(int(input())):
    test_code = input()
    if _ == 0:
        answer = list(test_code)
    for i, t in enumerate(test_code):
        if answer[i] != t:
            answer[i] = '?'
print(''.join(answer))