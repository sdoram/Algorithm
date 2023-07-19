mirror = [input() for _ in range(int(input()))]
mind = int(input())
if mind == 1:
	print("\n".join(mirror))
elif mind == 2:
	print("\n".join([i[::-1] for i in mirror]))
elif mind == 3:
	print("\n".join([i for i in mirror[::-1]]))
