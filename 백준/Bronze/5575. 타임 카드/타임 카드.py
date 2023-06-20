for _ in range(3):
    commute_list = list(map(int, input().split()))
    go_to_work = commute_list[:3]
    leave_work = commute_list[3:]
    go_to_work_second = go_to_work[0] * 3600 + go_to_work[1] * 60 + go_to_work[2]
    leave_work_second = leave_work[0] * 3600 + leave_work[1] * 60 + leave_work[2]
    total_second = leave_work_second - go_to_work_second
    print(
        *[
            total_second // 3600,
            total_second % 3600 // 60,
            total_second % 3600 % 60,
        ]
    )