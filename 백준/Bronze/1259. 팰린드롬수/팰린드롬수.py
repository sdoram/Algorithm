def palindrome(num):
    for i1, n1 in enumerate(num):
        for i2, n2 in enumerate(num[::-1]):
            if i1 == i2:
                if n1 != n2:
                    return 'no'

    return 'yes'


while True:
    num = input()
    if num == '0':
        break
    print(palindrome(num))