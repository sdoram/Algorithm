import sys, string

input = sys.stdin.readline

alphabet = list(string.ascii_letters+'-')
word_dict = {}

while True:
    sentence = input().rstrip()
    word = ''
    for s in sentence:
        if s not in alphabet:
            # 각 길이별 처음 나온 단어만 저장
            if len(word) not in word_dict:
                word_dict[len(word)] = word.lower()
            word = ''
        else:
            word += s
    if len(word) not in word_dict and word != 'E-N-D':
        word_dict[len(word)] = word.lower()

    # 마지막부분이 E-N-D인지 확인
    if 'E-N-D' == sentence[-5:]:
        break
print(word_dict[max(word_dict)])