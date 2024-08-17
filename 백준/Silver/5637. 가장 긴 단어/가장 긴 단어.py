import sys, string

input = sys.stdin.readline

alphabet = list(string.ascii_letters+'-')
word_dict = {}

while True:
    sentence = input().rstrip()
    word = ''
    for s in sentence:
        if s not in alphabet:
            if len(word) not in word_dict:
                word_dict[len(word)] = word.lower()
            word = ''
        else:
            word += s
    if 'E-N-D' == sentence[-5:]:
        break
print(word_dict[max(word_dict)])