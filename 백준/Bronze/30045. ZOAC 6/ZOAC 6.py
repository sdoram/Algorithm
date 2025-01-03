count = 0
for _ in range(int(input())):
    sentence = input()
    if '01' in sentence or 'OI' in sentence:
        count += 1
print(count)
    