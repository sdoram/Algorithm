alphabet = input()
alphabet_dict = {k: True for k in alphabet if k in ["M", "O", "B", "I", "S"]}
count = sum([(alphabet_dict.get(n, False)) for n in alphabet_dict.keys()])
print("YES" if count == 5 else "NO")