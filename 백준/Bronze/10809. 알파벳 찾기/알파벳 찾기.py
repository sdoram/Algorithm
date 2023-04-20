alpah_list = [-1]*26
word = input()

for idx, str_ in enumerate(word):
    alpah_index = ord(str_) - ord('a')
    if alpah_list[alpah_index] == -1:
        alpah_list[alpah_index] = idx
        
print(*alpah_list)
