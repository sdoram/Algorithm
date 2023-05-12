import sys

commute_list = []
for _ in range(int(input())):
    commute = sys.stdin.readline().split()
    if commute[1] == "enter":
        commute_list.append(commute[0])
    elif commute[1] == "leave":
        commute_list.remove(commute[0])
print(*sorted(commute_list, reverse=True), sep="\n")