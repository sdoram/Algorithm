BOARD = input()
A, B = "AAAA", "BB"
ANSWER = BOARD.replace("XXXX", A).replace("XX", B)
if "X" not in ANSWER:
    print(ANSWER)
else:
    print(-1)