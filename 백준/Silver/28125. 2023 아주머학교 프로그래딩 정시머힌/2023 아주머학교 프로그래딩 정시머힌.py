replace_spelling = {
    "a":"@"
    ,"c":"["
    ,"i":"!"
    ,"j":";"
    ,"n":"^"
    ,"o":"0"
    ,"t":"7"
    ,"w":"\\\\'"
    ,"v":"\\'"
    }
for _ in range(int(input())):
    word = input()
    count = 0
    for key, value in replace_spelling.items():
        if value in word:
            count += word.count(value)
            word = word.replace(value, key)
    print(word if len(word) > count*2 else "I don't understand")