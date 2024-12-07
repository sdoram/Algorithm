import string
alphabet = list(string.ascii_lowercase)
for _ in range(int(input())):
    password = input()
    alphabet_count = dict()
    for alpha in alphabet:
        if password.count(alpha) not in alphabet_count:
            alphabet_count[password.count(alpha)] = alpha
        else:
            alphabet_count[password.count(alpha)] += alpha
    probably_e = alphabet_count[max(alphabet_count)]
    print(probably_e if len(probably_e) == 1 else "?")