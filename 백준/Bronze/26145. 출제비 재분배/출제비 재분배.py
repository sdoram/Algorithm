N, M = map(int, input().split())
S = list(map(int, input().split()))
fee_dict = {nm:0 for nm in range(N+M)}
for n in range(N):
    fee = list(map(int, input().split()))
    fee_dict[n] += S[n] - sum(fee)
    for i, f in enumerate(fee):
        fee_dict[i] += f
        
for value in fee_dict.values():
    print(value, end=' ')