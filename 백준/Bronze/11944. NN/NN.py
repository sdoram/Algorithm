def NN(NM):
    answer = str(NM[0])*NM[0]
    
    return answer if len(answer) <= NM[1] else answer[:NM[1]]
    
print(NN(list(map(int, input().split()))))