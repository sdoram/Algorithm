bill_dict = {
"Paper" :	57.99,
"Printer" :	120.50,
"Planners" :	31.25,
"Binders" :	22.50,
"Calendar" :	10.95,
"Notebooks" :	11.20,
"Ink" :	66.95,
}
total = 0

while True:
    t = input()
    if t == 'EOI':
        print(f'${total}')
        break
    else:
        total += bill_dict[t]