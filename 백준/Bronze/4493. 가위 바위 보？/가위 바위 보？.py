import sys
for _ in range(int(sys.stdin.readline())):
    SCORE = 0
    for _ in range(int(sys.stdin.readline())):
        P1, P2 = sys.stdin.readline().split()
        if (P1 == 'R' and P2 == 'S') or (P1 == 'S' and P2 == 'P') or (P1 == 'P' and P2 == 'R'):
            SCORE += 1
        elif (P2 == 'R' and P1 == 'S') or (P2 == 'S' and P1 == 'P') or (P2 == 'P' and P1 == 'R'):
            SCORE -= 1
    if SCORE == 0:
        print('TIE')
    else:
        print('Player 1' if SCORE > 0 else 'Player 2')