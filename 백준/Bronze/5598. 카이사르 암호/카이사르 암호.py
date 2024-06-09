import string
 
alphabet = list(string.ascii_uppercase)
password_alphabet = list(string.ascii_uppercase[3:] + string.ascii_uppercase[:3])
print(''.join([alphabet[password_alphabet.index(a)] for a in input()]))
