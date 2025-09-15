for _ in range(int(input())):
    word = input()
    print(''.join(['_'+w.lower() if w.isupper() else w for w in word[0].lower()+word[1:]]))