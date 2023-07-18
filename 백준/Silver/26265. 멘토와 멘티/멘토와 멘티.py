from sys import stdin

mentor_mentee = [stdin.readline().split() for _ in range(int(stdin.readline()))]
mentor_mentee = sorted(mentor_mentee, key=lambda x: x[1], reverse=True)
mentor_mentee = sorted(mentor_mentee, key=lambda x: x[0])
for i in mentor_mentee:
    print(" ".join(i))
