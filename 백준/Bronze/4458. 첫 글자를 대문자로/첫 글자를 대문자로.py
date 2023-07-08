for _ in range(int(input())):
    sentence = input()
    print(
        "".join(
            [
                word.upper() if index == 0 else word
                for index, word in enumerate(sentence)
            ]
        )
    )
