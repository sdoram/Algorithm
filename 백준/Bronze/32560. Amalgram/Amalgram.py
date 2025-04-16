import string
alphabet = list(string.ascii_lowercase)
a = input()
b = input()
alphabet_dict = {alpha: max(a.count(alpha), b.count(alpha)) for alpha in alphabet}
print(''.join([key * value for key, value in alphabet_dict.items()]))