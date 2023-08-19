for i in range(1, int(input()) + 1):
    hobbit, human1, elf, dwarf, eagle, wizard1 = map(int, input().split())
    orc, human2, wolf, goblin, urukhai, troll, wizard2 = map(int, input().split())
    G = hobbit * 1 + human1 * 2 + elf * 3 + dwarf * 3 + eagle * 4 + wizard1 * 10
    S = (
        orc * 1
        + human2 * 2
        + wolf * 2
        + goblin * 2
        + urukhai * 3
        + troll * 5
        + wizard2 * 10
    )
    if S == G:
        print(f"Battle {i}: No victor on this battle field")
    elif S < G:
        print(f"Battle {i}: Good triumphs over Evil")
    elif S > G:
        print(f"Battle {i}: Evil eradicates all trace of Good")
