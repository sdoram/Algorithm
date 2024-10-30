ML, MR, TL, TR = input().split()
CHECK = True

if ML == MR:
    if ML == 'R' and (TL == 'P' or TR == 'P') or ML == 'S' and (TL == 'R' or TR == 'R') or ML == 'P' and (TL == 'S' or TR == 'S'):
        print('TK')
        CHECK = False
if TL == TR:
    if TL == 'R' and (ML == 'P' or MR == 'P') or TL == 'S' and (ML == 'R' or MR == 'R') or TL == 'P' and (ML == 'S' or MR == 'S'):
        print('MS')
        CHECK = False
if CHECK:
    print('?')