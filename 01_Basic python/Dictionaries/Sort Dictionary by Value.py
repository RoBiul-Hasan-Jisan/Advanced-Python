data = {'a': 10, 'b': 50, 'c': 30}
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print(sorted_data)