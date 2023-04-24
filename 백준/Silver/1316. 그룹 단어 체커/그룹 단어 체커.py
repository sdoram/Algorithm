a = int(input())
word_list = []
while a > 0:
    a -= 1
    word = input()
    word_list.append(word)
    word_dict = {}
    for w in range(len(word)):
        if word[w] not in word_dict:
            word_dict[word[w]] = 1
        else:
            word_dict[word[w]] += 1
        # 단어가 바뀌는 구간
        if w != 0 and word[w] != word[w-1]:
            # 단어가 첫 등장이 아니면
            if word_dict[word[w]] != 1:
                word_list.pop()
                break
print(len(word_list))
