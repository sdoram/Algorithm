word_dict = {}
for _ in range(int(input())):
    word = input()
    if len(word) not in word_dict:
        word_dict[len(word)] = [word]
    else:
        word_dict[len(word)] += [word]

for num in sorted(word_dict):
    for word in sorted(set(word_dict[num])):
        print(word)