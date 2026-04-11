dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 50, 'c': 30}

merged = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in dict1.keys() | dict2.keys()}

print(merged)