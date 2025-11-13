hot_dict = {
'Poblano':	1500,
'Mirasol':	6000,
'Serrano':	15500,
'Cayenne':	40000,
'Thai':	75000,
'Habanero':	125000}

print(sum([hot_dict[input()] for _ in range(int(input()))]))