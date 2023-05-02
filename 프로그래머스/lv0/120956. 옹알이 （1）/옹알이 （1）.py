def solution(babbling):
    # "aya", "ye", "woo", "ma"을 최대 1번까지 활용해 만든 조합만 발음 가능
    answer = 0
    word_list = ['aya', 'ye','woo','ma']
    for bab in babbling:
        in_word = []
        for word in word_list:
            if word in bab:
                in_word.append(word)
        if len(''.join(in_word)) == len(bab):
            answer += 1
    return answer