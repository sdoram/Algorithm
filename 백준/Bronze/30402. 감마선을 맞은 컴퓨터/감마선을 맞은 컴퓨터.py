cat = ''
for _ in range(15):
    photo = input().split()
    if 'w' in photo:
        cat = 'chunbae'
    elif 'b' in photo:
        cat = 'nabi'
    elif 'g' in photo:
        cat = 'yeongcheol'
print(cat)