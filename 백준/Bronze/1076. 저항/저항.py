a = input()
b = input()
c = input()

color_dict = {
    'black': [0, 1],
    'brown': [1, 10],
    'red':	[2, 100],
    'orange': [3, 1000],
    'yellow': [4, 10000],
    'green': [5, 100000],
    'blue':	[6, 1000000],
    'violet': [7, 10000000],
    'grey':	[8, 100000000],
    'white': [9, 1000000000]
}
print((color_dict[a][0]*10 + color_dict[b][0])*color_dict[c][1])