while True:
    try:
        word = input()
        l = len([w for w in word if w.islower()])
        u = len([w for w in word if w.isupper()])
        d = len([w for w in word if w.isdigit()])
        s = word.count(' ')
        print(l, u, d, s)
    except EOFError:
        break