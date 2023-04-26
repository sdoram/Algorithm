star = int(input())
count = 1
while count <= star:
    print(('*'*count).rjust(star), '*'*(count-1), sep='')
    count += 1