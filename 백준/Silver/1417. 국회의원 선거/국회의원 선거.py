import sys
input = sys.stdin.readline

def vote_corruption(n):
    my_vote = int(input())
    if n == 1:
        return print(0)
    other_vote = [int(input()) for _ in range(n-1)]
    count = 0
    while my_vote <= max(other_vote):
        my_vote += 1
        count += 1
        other_vote[other_vote.index(max(other_vote))] -= 1
        
    return print(count)

vote_corruption(int(input()))
        