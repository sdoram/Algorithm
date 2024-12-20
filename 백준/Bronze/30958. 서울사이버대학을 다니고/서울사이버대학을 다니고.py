import string
alphabet = list(string.ascii_lowercase)
input()
logo_song = input()
print(max([logo_song.count(a) for a in alphabet]))