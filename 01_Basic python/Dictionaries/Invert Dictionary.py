data = {'a': 10, 'b': 11, 'c': 20}

swapped = {}
for k, v in data.items():
    swapped.setdefault(v, []).append(k)

print(swapped)