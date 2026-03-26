d = {'a': 5, 'b': 8, 'c': 3, 'd': 10}


for key in d:
    if d[key] % 2 == 0:
     d[key] = 0


print(d)