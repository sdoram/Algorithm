not_mirror = ['a', 'c', 'e', 'f', 'g', 'h', 'j', 'k' ,'l' , 'm', 'n', 'r', 's', 't', 'u', 'y', 'z']
while True:
    x = input()
    mirror_word = ''
    if x == '#':
        break
    if [i for i in x if i in not_mirror]:
        print('INVALID')
    else:
        for i in x:
            if i == 'b':
                mirror_word += 'd'
            elif i == 'd':
                mirror_word += 'b'
            elif i == 'p':
                mirror_word += 'q'
            elif i == 'q':
                mirror_word += 'p'
            else:
                mirror_word += i
        print(mirror_word[::-1])