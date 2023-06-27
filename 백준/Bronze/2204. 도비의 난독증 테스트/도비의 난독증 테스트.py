while True:
    n = int(input())
    if n == 0:
        break
    print(
        sorted([input() for _ in range(n)], key=lambda alpha_list: alpha_list.upper())[
            0
        ]
    )