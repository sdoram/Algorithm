def sudoku_check():
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    sudoku_dict = {}
    for i in range(0,3):
        for j in range(0,3):
            sudoku_dict[i,j] = []
            
    for width in sudoku:
        if len(set(width)) != 9:
            return 1
        
    for hight in range(9):
        hight_set = set()
        for h in range(9):
            hight_set.add(sudoku[h][hight])
        if len(hight_set) != 9:
            return 1
        
    for i in range(9):
        for j in range(9):
            sudoku_dict[i//3,j//3].append(sudoku[i][j])
    
    for value in sudoku_dict.values():
        if len(set(value)) != 9:
            return 1
    return 0

N = int(input())
for n in range(1, N+1):
    print(f'Case {n}: INCORRECT' if sudoku_check() else f'Case {n}: CORRECT')
    if n != N:
        input()

