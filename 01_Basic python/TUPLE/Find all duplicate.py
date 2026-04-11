t = (1, 2, 3, 2, 4, 1, 5, 3)

# Easy way to find duplicates
duplicates = tuple(set(x for x in t if t.count(x) > 1))

print("Duplicate elements:", duplicates)