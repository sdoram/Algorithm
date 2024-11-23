word = input()
print(word.count('JOI'))
print(sum([1 for i in range(len(word)-2) if word[i:i+3] == "IOI"]))