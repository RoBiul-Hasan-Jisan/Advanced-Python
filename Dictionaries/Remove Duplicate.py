data = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

seen = set()
new_dict = {k: v for k, v in data.items() if not (v in seen or seen.add(v))}

print(new_dict)



data = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

# Remove duplicates (keeps last key for each value)
new_dict = dict(zip(dict.fromkeys(data.values()), data.keys()))

print(new_dict)