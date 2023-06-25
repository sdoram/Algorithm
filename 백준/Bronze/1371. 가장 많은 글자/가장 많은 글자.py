alpha_list = [0] * 26
while True:
    try:
        word = input()
        for w in word:
            if ord(w) != 32:
                alpha_list[ord(w) - 97] += 1
    except EOFError:
        print(
            "".join(
                sorted(
                    [
                        chr(i + 97)
                        for i, a in enumerate(alpha_list)
                        if a == max(alpha_list)
                    ]
                )
            )
        )
        break
