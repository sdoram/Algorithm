a = int(input())
while_count = 0
while a > while_count:
    while_count += 1
    quiz = input()
    quiz_list = quiz.split('X')
    answer = 0
    for i in quiz_list:
        count = 0
        for num in i:
            count += 1
            answer += count
    print(answer)
