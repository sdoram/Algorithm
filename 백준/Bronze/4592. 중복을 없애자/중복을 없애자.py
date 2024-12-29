while True:
    submission = list(input().split())
    if submission == ['0']:
        break
    submission_list = [submission[1]]
    current_sub = submission[1]
    for sub in submission[2:]:
        if current_sub != sub:
            submission_list.append(sub)
            current_sub = sub
    submission_list.append('$')
    print(' '.join(submission_list))