P, D = 0, 0
COUNT = int(input())
while COUNT:
    if input() == "P":
        P += 1
    else:
        D += 1
    if P-2 == D or D-2 == P:
        print(f"{D}:{P}")
        break
    COUNT -= 1
if COUNT == 0:
	print(f"{D}:{P}")
