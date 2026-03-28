t = (1, 2, 3, 2, 4, 1, 5, 3, 6)

unique_elements = tuple(x for x in t if t.count(x) == 1)

print("Unique elements:", unique_elements)