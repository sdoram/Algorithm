n = int(input())
VOTES = input()
A = VOTES.count("A")
B = VOTES.count("B")
if A == B:
    print("Tie")
else:
    print("A" if A > B else "B")