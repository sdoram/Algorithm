words = input()
num = (len(words)-1)//10+1
for n in range(1, num+1):
    start = (n-1)*10
    end = n*10
    print(words[start:end])