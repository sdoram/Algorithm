import sys

input = sys.stdin.readline

def chat():
    count = 0
    users = set()
    for _ in range(int(input())):
        user = input().rstrip()
        if user not in users:
            users.add(user)
        elif user in users and user =='ENTER':
            count += len(users)-1
            users = set(['ENTER'])
    if len(users) != 0:
        count += len(users)-1
    return count

print(chat())