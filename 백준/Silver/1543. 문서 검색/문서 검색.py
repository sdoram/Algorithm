def word_search(WORD, SEARCH):
    COUNT = 0
    while True:
        try:
            WORD = WORD[WORD.index(SEARCH)+len(SEARCH):]
            COUNT += 1
        except ValueError:
            return print(COUNT)
        
word_search(input(), input())