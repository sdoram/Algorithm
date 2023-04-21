n = int(input())
for _ in range(n):
    num, word = input().split()
    num = int(num)
    new_word = ''
    for w in word:
        new_word += w * num
    print(new_word)