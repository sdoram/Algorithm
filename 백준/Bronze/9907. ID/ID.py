n = input()
SN = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z']
print(SN[(2 * int(n[0]) + 7 * int(n[1]) + 6 * int(n[2]) + 5 * int(n[3]) + 4 * int(n[4]) + 3 * int(n[5]) + 2 * int(n[6])) % 11])