N = int(input())
vote = list(map(int, input().split()))
print('INVALID' if (N+1) // 2 <= vote.count(0) else 'APPROVED' if sum(vote) > 0 else 'REJECTED')