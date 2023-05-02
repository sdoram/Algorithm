def solution(numLog):
    num_dict = {1:'w',10:'d',-1:'s',-10:'a'}    
    return ''.join([num_dict[num-numLog[i]] for i,num in enumerate(numLog[1:])])