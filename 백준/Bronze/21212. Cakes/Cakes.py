material_list = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    material_list.append(y//x)
print(min(material_list))